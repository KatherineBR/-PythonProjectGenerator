import random

verbList = ["to organize", "using", "to create", "to teach"]
thingList = ["user input", "something useless", "art", "an api", "data", "a new language"]
whereList = [" chrome extension", " website", "n ios app", " game"]

def pick():
   verb = random.choice(verbList)
   thing = random.choice(thingList)
   where = random.choice(whereList)
   return "make a" + where + " " + verb + " " + thing

project = input("How many project ideas would you like? ")

try:
  num = int(project)
  print("ideas:")
  for i in range(num):
    print(pick())
except:
  print("invalid number input")
  print("one project idea is: " + pick())
