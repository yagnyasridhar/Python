from flask import Flask,render_template,request,url_for, redirect

app = Flask("request response")
cnt = {0:{"title":"Jinga2 example", "content":"Sample program for Jinga2"},
404:{"title":"404", "content":"Page not found"}}

@app.route("/")
def home():
    return "Your first page"

@app.route("/form")
def form():
    return render_template("3.jinga2")

@app.route("/redirected/<int:id>")
def redirected(id):
    dct = cnt.get(id)
    if not dct:
        dct = cnt.get(404)
        return render_template("404.jinga2",post = dct)
    return render_template("2.jinga2",post = dct)

@app.route("/post")
def post():
    title = request.args.get("title")
    content = request.args.get("content")
    cnt[1] = {"title":title, "content":content}
    return redirect(url_for("redirected", id = 1))

if(__name__ == "__main__"):
    app.run(debug=True)