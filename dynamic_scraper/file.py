from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv


def save_to_file(file_name, keyword):
    p = sync_playwright().start()

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(f"https://www.wanted.co.kr/search?query={keyword}&tab=position")

    for x in range(4):
        page.keyboard.down("End")
        time.sleep(5)

    content = page.content()

    p.stop()

    soup = BeautifulSoup(content, "html.parser")

    jobs = soup.find_all("div", class_="JobCard_container__FqChn")

    jobs_db = []

    for job in jobs:
        link = f"https://www.wanted.co.kr{job.find('a')['href']}"
        title = job.find("strong", class_="JobCard_title__ddkwM").text
        company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
        # location = job.find() # location은 없어짐;
        reward = job.find("span", class_="JobCard_reward__sdyHn").text
        job = {
            "title": title,
            "company_name": company_name,
            "reward": reward,
            "link": link,
        }
        jobs_db.append(job)

    file = open(f"./dynamic_scraper/{file_name}.csv", "w", encoding="utf-8", newline="")
    writer = csv.writer(file)
    writer.writerow(
        [
            "Title",
            "Company",
            "Reward",
            "Link",
        ]
    )

    for job in jobs_db:
        writer.writerow(job.values())

    file.close()
