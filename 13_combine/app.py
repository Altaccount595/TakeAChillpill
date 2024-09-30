# Jonathan Metzler-Kyle Lee-Suhana Kumar - MLK
# SoftDev
# Sep 2024

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

@app.route("/wdywtbwygp") 
def test_tmplt():
    return render_template('tablified.html', foo="fooooo", oogada= "combining elements of flask and html", boogada="Jonathan Metzler-Kyle Lee-Suhana Kumar - MLK")


if __name__ == "__main__":
    app.debug = True
    app.run()

