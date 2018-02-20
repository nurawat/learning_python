##
# Basic Learner type
#
##

# ip_address = input("Please Enter IP address : ")
# print(ip_address.count("."))


ip_address = ["127.0.0.1", "192.168.0.1", "192.168.1.1"]

for single_IP in ip_address:
  print("IP given is {}".format(single_IP))

### List
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]
numbers = even + odd
l_numbers = numbers
numbers.sort(reverse = True)
print(numbers is even)
if sorted(l_numbers) == numbers:
  print("YES")
else:
  print("NO")

print(list("Hi, This is arun"))



dummy = "this is a test"

print(dummy.split())



###### range
print("#######################")
print(list(range(0,10,1)))
print(list(range(0,10,2)))
