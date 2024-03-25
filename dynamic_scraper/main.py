# 6.13 Code Challenge

from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

# p = sync_playwright().start()

# # 브라우저 초기화
# # headless=True 가 default
# # headless=False로 바꾸면 브라우저가 보임
# browser = p.chromium.launch(headless=False)

# # 새로운 탭 열기
# page = browser.new_page()

# # 사이트로 이동
# page.goto("https://www.wanted.co.kr/jobsfeed")

# time.sleep(3)

# # class명으로 선택하여 클릭
# page.click("button.Aside_searchButton__Xhqq3")
# # page.locator("button.Aside_searchButton__Xhqq3").click()

# time.sleep(3)

# # placeholder 내용으로 선택하여 빈칸에 내용 채움
# page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

# time.sleep(3)

# # Enter 키를 누른 효과
# page.keyboard.down("Enter")

# time.sleep(5)

# # id명으로 선택하여 클릭
# page.click("a#search_tab_position")


# time.sleep(5)
def job_scraper(keyword):
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

    # mode = r 이 default
    # 한글깨짐해결 : encoding="utf-8"
    # windows 실행 시 빈 줄 추가 제거 : newline=""
    file = open(
        f"./dynamic_scraper/{keyword}_jobs.csv", "w", encoding="utf-8", newline=""
    )
    writer = csv.writer(file)
    # writer.writerow는 list를 받음
    writer.writerow(
        [
            "Title",
            "Company",
            "Reward",
            "Link",
        ]
    )

    # dictionary의 value만 추출하여 list 생성 : dictionary_name.values()
    for job in jobs_db:
        writer.writerow(job.values())


keywords = [
    "flutter",
    "nextjs",
    "kotlin",
]

for keyword in keywords:
    job_scraper(keyword)
