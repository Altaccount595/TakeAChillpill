"""
Jonathan Metzler
No Z's
SoftDev
K<nn> -- <Title/Topic/Summary... (Aim for concision, brevity, CLARITY. Write to your future self...)>
2024-09-13
time spent: 0.25
"""
import random
krewes = {3:['Jonthan','Alex','Naf'], 42:['Jonthan','Alex','Naf'], 888:['Jonthan','Alex','Naf']}

def randoselect():
    x=int(random.random()*3)
    lis=list (krewes.keys())
    z=int(random.random()*3)
    print((krewes.get(lis[x]))[z])
randoselect()