#1

def greet(language):
  if language=='english':
    return('Welcome')
  elif language=='czech':
    return('Vitejte')
  elif language=='danish':
    return('Velkomst')
  elif language=='dutch':
    return ('Welkom')
  elif language=='estonian':
    return('Tere tulemast')
  elif language=='finnish':
    return('Tervetuloa')
  elif language=='flemish':
    return('Welgekomen')
  elif language=='french':
    return('Bienvenue')
  elif language=='german':
    return('Willkommen')
  elif language=='irish':
    return('Failte')
  elif language=='italian':
    return('Benvenuto')
  elif language=='latvian':
    return ('Gaidits')
  elif language=='lithuanian':
    return ('Laukiamas')
  elif language=='polish':
    return ('Witamy')
  elif language=='spanish':
    return('Bienvenido')
  elif language=='swedish':
    return('Valkommen')
  elif language=='welsh':
    return('Croeso')
  else:
    return('Welcome')
  

#2

la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals


#3

def two_sort(array):
    return '***'.join(min(array))


#4

def people_with_age_drink(age):
    if age <= 13:
        beverage = 'toddy'
    elif age > 13 and age <= 17:
        beverage = 'coke'
    elif age > 17 and age <= 20:
        beverage = 'beer'
    elif age > 20:
        beverage = 'whisky'
    return 'drink ' + beverage



#5

def solution(a, b):
    if len(a)>len(b):
        return(b+a+b)
    else:
        return(a+b+a)



#6

def fix_the_meerkat(arr):
    arr.reverse()
    return arr