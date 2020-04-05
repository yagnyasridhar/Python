from flask import Flask,render_template,request,url_for, redirect

app = Flask("request response")
cnt = {0:{"title":"Jinga2 example", "content":"Sample program for Jinga2"},
404:{"title":"404", "content":"Page not found"}}

@app.route("/")
def home():
    return "Your first page"

@app.route("/form", methods = ["GET", "POST"])
def form():
    if(request.method == "POST"):
        title = request.form.get("title")
        print(title)
        content = request.form.get("content")
        cnt[1] = {"title":title, "content":content}
        print(cnt[1])
        return redirect(url_for("redirected", id = 1))
    return render_template("4.jinga2")

@app.route("/redirected/<int:id>")
def redirected(id):
    dct = cnt.get(id)
    if not dct:
        dct = cnt.get(404)
        return render_template("404.jinga2",post = dct)
    return render_template("2.jinga2",post = dct)

if(__name__ == "__main__"):
    app.run(debug=True)