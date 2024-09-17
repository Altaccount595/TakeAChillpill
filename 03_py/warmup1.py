# Naf (Nafiyu Murtaza), Alex (Sasha Murokh), Jonathan (Jonathan Metzler)
# No Z's In Our Name
# SoftDev
# K03 -- Warmups
# 2024-09-17
# Time: N/A

# READ: The function names indicate the problem in Codingbat.

def sleep_in(weekday, vacation):
  return (not weekday) or vacation

def monkey_trouble(a_smile, b_smile):
  return (a_smile and b_smile) or (not a_smile and not b_smile)

def sum_double(a, b):
  if (a==b):
    return 2*(a+b)
  else:
    return a+b

def diff21(n):
  x = 21-n
  if (x<0):
    return x*-2
  else:
    return x

def parrot_trouble(talking, hour):
  return talking and (hour<7 or hour>20)

def makes10(a, b):
  return (a==10) or (b==10) or (a+b==10)

def near_hundred(n):
  return (abs(100-n)<=10) or (abs(200-n)<=10)

def pos_neg(a, b, negative):
  if negative:
    return (a<0) and (b<0)
  else:
    return a*b<0

def not_string(str):
  if (str[:3]=='not'):
    return str
  else:
    return 'not ' +str

def missing_char(str, n):
  return str[:n] + str[1+n:]

def front_back(str):
  if len(str)<=1:
    return str
  if len(str)==2:
    return str[1]+str[0]
  return str[len(str)-1]+str[1:len(str)-1]+str[0]

def front3(str):
  return(str[:3]*3)
