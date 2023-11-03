from flask import Flask, render_template, url_for, request

app = Flask(__name__)

menu = [{"name": "Set", "url": "install-flask"},
        {"name": "First", "url": "first-app"},
        {"name": "Feedback", "url": "contact"}
]

@app.route('/index')
@app.route('/')
def index():
    return render_template("index.html", title ="Про Flask", menu=menu)

@app.route('/about')
def about():
    return render_template("about.html", title = "О сайте", menu=menu)

@app.route("/contact", methods = ["POST", "GET"])
def contact():
    if request.method == 'POST':
        print(request.form)
    return render_template("contact.html", title = "Feedback", menu=menu)

# Конверторы path, int, float
@app.route("/profile/<path:username>")
def profile(username):
    return f"Пользователь: {username}"

if __name__ == "__main__":
    app.run(debug=True)