# 6.8 PlayWright

from playwright.sync_api import sync_playwright

p = sync_playwright().start()

# headless=True 가 default
browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://google.com")

page.screenshot(path="./dynamic_scraper/screenshot.png")
