# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)          # ...debug is off

@app.route("/")                # ...
def hello_world():
    print(__name__)            # ...prints "__main__"
    return "No hablo queso!"   # ...site says "No hablo queso!"

app.run()                      # ...
                
