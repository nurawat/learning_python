### Dictionaries and sets.


createDictionaries = {
  "arun": "rawat",
  "amit": "auddy",
  "jack": "afron",
}
print(createDictionaries)
print(createDictionaries["amit"])



### enter and display the dictionary

while True:
  dict_key = input("Enter the key name : ")
  dict_data =  input("Enter the value for it : ")
  createDictionaries[dict_key] = dict_data

  if input("Want more(y/n) :") in "n":
    break

print(createDictionaries.keys())


print(tuple(createDictionaries.items()))
