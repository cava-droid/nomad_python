# 6.2 BeautifulSoup

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
jobs = soup.find("section", class_="jobs").find_all("li")

print(jobs)
