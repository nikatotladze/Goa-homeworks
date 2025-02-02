#1

def who_is_paying(name):
    return [name,name[0:2]] if len(name)>2 else [name]


#2

def oddCount(n):
    return n // 2


#3

def is_uppercase(inp):
    return inp.upper()==inp

#4

def grader(x):
  if 0.9 <= x <= 1: return "A"
  elif 0.8 <= x < 0.9: return "B"
  elif 0.7 <= x < 0.8: return "C"
  elif 0.6 <= x < 0.7: return "D"
  else: return "F"


#5

def ifChuckSaysSo():
    return 0