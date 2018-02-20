name = input("Enter your Name: ")
age =  int(input("How old are you, {}? : ".format(name)))
print(name + " you are " + str(age) + " years old.")


if age >= 18 and age <60:
  print("You can vote.")
elif age >=60:
  print("You old man.")
else:
  print("You can vote later.")
