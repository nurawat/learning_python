_author_ = 'arun'

name = input("Enter your name :")
age = int(input("Enter your age :"))

if 18> age <31:
  print("Welcome to Holiday")

elif age <=18:
  print("You are {} short".format(19 - age))

else:
  print("You are over {} holiday ahead".format(age - 30))