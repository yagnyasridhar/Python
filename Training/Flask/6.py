from flask import Flask,render_template,request,url_for, redirect
from cachetools import TTLCache, cached
app = Flask("request response")
emp = {123:{"Employee Name":"Jinga2"},
234:{"Employee Name":"student"}}

@app.route("/")
def home():
    return render_template("5.jinga2")

@app.route("/employee")
@cached(cache=TTLCache(maxsize = 2, ttl=900))
def employee():
    return render_template("6.jinga2", data = emp)

if(__name__ == "__main__"):
    app.run(debug=True)