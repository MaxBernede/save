#https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'