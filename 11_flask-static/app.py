# Clyde 'Thluffy' Sinclair
# SoftDev
# Sep 2024

# DEMO
# basics of /static folder
import random
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<a href='http://127.0.0.1:5000/static/fixie.html'>oogada boogada</a>"


@app.route("/static/foo.html")
def h():
    return str(random.random())

@app.route("/static/fixie.html")
def g():
    text=open('static/fixie.html')
    return text



if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()