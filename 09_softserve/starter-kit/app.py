import random
from flask import Flask
app = Flask(__name__)                 

@app.route("/")

def generateRandom():
    occupations = {}
    with open('occupations.csv') as text:
        reader = text.read()
        reader = reader.split('\n')
        for row in range(len(reader)-2):
            if '"' in reader[row+1]:
                reader[row+1] = reader[row+1].split('",')
                reader[row+1][0] = reader[row+1][0][1:]
            else:
                reader[row+1] = reader[row+1].split(',')
            occupations[reader[row+1][0]]=float(reader[row+1][1])
    generated = random.random()*99.8
    for key in occupations.keys():
        if (generated<0):
            return(str(key)+', ' +str(occupations[key]))
        else:
            generated-=occupations[key]
    return("error")

def main():         
    return generateRandom()

app.debug = True
app.run()