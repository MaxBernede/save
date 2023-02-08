from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"