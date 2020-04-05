from flask import Flask, render_template

app = Flask("HTML")
cnt = {0: {"title":"HTML Rendering", "content":"This is my first HTML page"}}

@app.route("/<int:id>")
def home(id):
    return render_template("1.html", content = cnt.get(id))

if(__name__ == "__main__"):
    app.run(debug=True)