# create flask app - done
# create template html files
# create static css 
# bring images into static
# connect it
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(port=5003, debug=True)