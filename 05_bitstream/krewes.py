import random
krewes = []
def pickrandom():
    opened = open("krewes.txt", "r")
    lst = opened.read().split("@@@")
    for item in lst[:-1]:
        item = item.split("$$$")
        krewes.append({'pd': item[0], 'name': item[1], 'ducky': item[2]})
    x = int(random.random()*len(krewes))
    print(krewes[x])
    
pickrandom()