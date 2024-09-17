# Naf (Nafiyu Murtaza), Alex (Sasha Murokh), Jonathan (Jonathan Metzler)
# No Z's In Our Name
# SoftDev
# K03 -- Warmups
# 2024-09-17
# Time: N/A

# READ: The function names indicate the problem in Codingbat.

def string_times(str, n):
  return (str*n)

def front_times(str, n):
  return (str[:3]*n)

def string_bits(str):
  return str[::2]

def string_splosion(str):
  i = 0
  output = ''
  while (i<len(str)+1):
    output += str[0:i]
    i+=1
  return output


