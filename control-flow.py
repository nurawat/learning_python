_author_='dev'

name = input("Enter your name:")
print("your name is : "+ name)
print("Your name is : {}".format(name))


age=int(input("Enter your age: "))

if age>=18 and age<100:
  print("You can VOTE")

elif age >=100:
  print("You are lying GrandPA")

else:
  print("No Go grow up first")