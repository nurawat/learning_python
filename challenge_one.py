# This is the first challenge given by the UDEMY professsional where the question is
#
##################
# Ask user for name and age when bothe the values have been entereed, check if the person is the of the right age to go on an
# 18-30 holiday if they are over and under 31.
# If they are, welcom ethem to the holiday otherwise print a polite message refusing them entry.
##################

__author__ = 'Arun Rawat'

name = input("Enter your name : ")
age = int(input("Hi {}, Enter your age :".format(name)))

if age >=18 and age <31:
  print("Hello {}, Welcome to the holiday.".format(name))
elif age >=31:
  print("You are too OLD for holiday.")
else:
  print("Hey {}, You are short by {} years, Come back SOON".format(name,18-age))
