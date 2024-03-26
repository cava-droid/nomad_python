# 7.8 Cache

from flask import Flask, render_template, request, redirect
from dynamic_scraper.job_scraper import scrap_jobs
from file import save_to_file

app = Flask("JobScrapper")

db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        jobs = scrap_jobs(keyword)
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)


@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword is not db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])


app.run("127.0.0.1", debug=True)
