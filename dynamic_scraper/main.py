# 7.1 Hello Flask

from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv
from file import save_to_file

# keywords = [
#     "flutter",
#     "nextjs",
#     "kotlin",
# ]

# for keyword in keywords:
#     job_scraper(keyword)

keyword = input("What do you want to search for? ")
file_name = input("Input file name : ")

save_to_file(
    file_name=file_name,
    keyword=keyword,
)
