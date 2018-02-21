people = {
  "arun": "rawat",
  "amit": "auddy",
  "sachin": "tendulkar",
  "saurav": "ganguly"
}

## CREATES COPY OF THE DICTIONARIES

print(people)

career = {
  "basketball": "stephen curry",
  "jim carrie": "movie",
  "jonty rodes": "cricket",
  "lance armstrong": "cycle"
}

print(career)

print("*" * 40)

career.update(people)
print(career)


# use copy

backupPeople = people.copy()
backupCareer = career.copy()

print("*" * 40)

print(backupPeople)
print(backupCareer)
