##
# This program uses random no which will be guessed by the user if he is able to select a
# random number successfully
#

import random

highest = 10
answer = random.randint(1, highest)

print("Please Guess a number between 1 and {}".format(highest), end = ' ')
guess = int(input())

while guess != answer:
  print("Wrong Guess !!!, Please select another number:", end = ' ')
  guess = int(input())

print("Congratulations !!!, You have selected the correct number i.e. {}".format(guess))
