# 4.7 Requests

from requests import get

websites = (
  "google.com",
  "airbnb.com",
  "https://twitter.com",
  "facebook.com",
  "https://tiktok.com",        
)

for website in websites:
  if not website.startswith("https://"):
    # website = "https://" + website
    website = f"https://{website}"
  print(website)        