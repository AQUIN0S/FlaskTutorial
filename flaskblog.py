from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        "author": "Daniel Schimanski",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "4 May, 2019"
    },
    {
        "author": "Levi Schimanski",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "5 May, 2019"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("pages/home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("pages/about.html", title="About")

if __name__ == "__main__":
    app.run(debug=True)
