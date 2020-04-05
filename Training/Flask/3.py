from flask import Flask,render_template

app = Flask("Jinga")
cnt = {0:{"title":"Jinga2 example", "content":"Sample program for Jinga2"},
404:{"title":"404", "content":"Page not found"}}
@app.route("/")
def home():
    return "Welcome!!!"

@app.route("/post/<int:id>")
def post(id):
    dct = cnt.get(id)
    if not dct:
        dct = cnt.get(404)
        return render_template("404.jinga2",post = dct)
    return render_template("2.jinga2",post = dct)

if(__name__ == "__main__"):
    app.run(debug=True)