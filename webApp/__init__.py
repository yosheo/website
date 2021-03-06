# __init__.py

#from flask import Flask
#app = Flask(__name__)
#@app.route("/")
#def hello():
#    return "Hello, I love Digital Ocean!"
#if __name__ == "__main__":
#    app.run()

from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", content="Testing")

@app.route('/projects')
def about():
    return render_template("projects.html")

@app.route('/website-documentation')
def website_doc():
    return render_template("website-documentation.html")

# @app.route("/")
# def home():
#     return render_template("index0.html")
#
# @app.route('/projects')
# def about():
#     return "Hello! This is the projects page!"
#
# @app.route('/contact')
# def contact():
#     return "Hello! This is the contact page!"

# @app.route('/<name>')
# def about(name):
#     return f"Hello from {name}"
#
# @app.route('/admin')
# def about():
#     return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
