'''
heading !!
disco:

qcc:

how this script works:
so far, this script only reads and processes the csv and populates a dictionary accordingly,
accounting for keys with quotes+commas and removing the heading and totals

'''
import pprint
import random
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
    #pprint.pp(occupations)

def generateRandom():
    generated = random.random()*99.8
    for key in occupations.keys():
        if (generated<0):
            return(str(key)+', ' +str(occupations[key]))
        else:
            generated-=occupations[key]
    return("error")
print(generateRandom()) 
    
