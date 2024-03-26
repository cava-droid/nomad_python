# 7.5 Arguments

from flask import Flask, render_template, request

app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def hello():
    keyword = request.args.get("keyword")
    return render_template("search.html", keyword=keyword)


app.run("127.0.0.1", debug=True)
