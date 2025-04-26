import random 
#declaration

#begin_code
number=int(input("digite o número secreto  "))

while number != random.randint(1,10):
  print("ERRADO OTÁRIO")
  number=int(input("digite dnv "))

print("ACERTOU! MISERAVEL")

#end_code
