_author_= 'dev'
age = 24
print("My age is" + str(age))
print("My age is {0} years and {1} months".format(age,1))

print("""Year has:{1} days {2}
seconds {1}"""
.format(1,365,54))

for i in range(1,12):
  print("output is {0}".format(i**2))

print("Pi is approaximately %12.5f" % (22/7))

for i in range(1,12):
  print("NO {0:2} squared is {1:4} and cubed is {2:4}".format(i, i**2, i**3))