# 6.4 Recap

import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

response = requests.get(url)

soup = BeautifulSoup(
    response.content,
    "html.parser",
)

# jobs = soup.find("section", id="category-2")

# class는 예약어이므로 class_로 사용
# [1:-1]로 첫번째 항목과 마지막 항목 삭제
jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

all_jobs = []

# text만 추출하려면 find()뒤에 .text 추가
for job in jobs:
    title = job.find("span", class_="title").text
    # region = job.find("span", class_="region").text
    company, position, region = job.find_all("span", class_="company")
    url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]
    # company = company.text
    # position = position.text
    # region = region.text
    # print(title, company, position, region, "------------------\n")
    job_data = {
        "title": title,
        "company": company.text,
        "position": position.text,
        "region": region.text,
        "url": f"https://weworkremotely.com{url}",
    }
    all_jobs.append(job_data)


print(all_jobs)
