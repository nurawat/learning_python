_author_ = 'arun'

# for i in range(1,20):
#   print(i)

number = "123,455"

for i in range(0, len(number)):
  if number[i] in '0123456789':
    print(number[i],end=' ')

