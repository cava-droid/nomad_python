# 6.8 PlayWright

from playwright.sync_api import sync_playwright

p = sync_playwright().start()

# 브라우저 초기화
# headless=True 가 default
# headless=False로 바꾸면 브라우저가 보임
browser = p.chromium.launch(headless=False)

# 새로운 탭 열기
page = browser.new_page()

# 구글사이트로 이동
page.goto("https://google.com")

# 페이지 스크린샷 저장
page.screenshot(path="./dynamic_scraper/screenshot.png")
