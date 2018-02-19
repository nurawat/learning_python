ip_address =  input("Enter the IP Address: ")
count = 0

for chars in ip_address:
 if chars in '.':
   count+=1

if count == 3:
  print("Yes")
else:
  print("No")
