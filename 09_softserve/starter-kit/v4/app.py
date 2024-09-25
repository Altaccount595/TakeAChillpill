# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ") #prints "the __name__ of this module is... " to terminal
    print(__name__)                     # prints "__main__" to terminal
    return "No hablo queso!"

if __name__ == "__main__":      # true if this file NOT imported   (so true in this case because __name__ is default "__main__" and unchanged
    app.debug = True            # enable auto-reload upon code change  - - - -debugger is active, debug pin printed
    app.run()
