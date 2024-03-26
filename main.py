# 7.8 Cache

from flask import Flask, render_template, request
from dynamic_scraper.job_scraper import scrap_jobs

app = Flask("JobScrapper")

db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword in db:
        jobs = db[keyword]
    else:
        jobs = scrap_jobs(keyword)
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)


app.run("127.0.0.1", debug=True)
