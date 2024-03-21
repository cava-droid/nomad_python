# 6.10 Interactivity

from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

p = sync_playwright().start()

# 브라우저 초기화
# headless=True 가 default
# headless=False로 바꾸면 브라우저가 보임
browser = p.chromium.launch(headless=False)

# 새로운 탭 열기
page = browser.new_page()

# 사이트로 이동
page.goto("https://www.wanted.co.kr/jobsfeed")

time.sleep(3)

page.click("button.Aside_searchButton__Xhqq3")
# page.locator("button.Aside_searchButton__Xhqq3").click()

time.sleep(3)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

time.sleep(3)

page.keyboard.down("Enter")

time.sleep(5)

page.click("a#search_tab_position")

time.sleep(5)

for x in range(4):
    page.keyboard.down("End")
    time.sleep(5)

content = page.content()

p.stop()

soup = BeautifulSoup(content, "html.parser")
