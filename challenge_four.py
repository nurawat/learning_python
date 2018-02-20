# #
# whatever elemets that are in the menu should be printed individually
# rather than in a array type
#

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

#print(menu)


# Displaying each entry different

for meal in menu:
  if not "spam" in meal:
    for items in meal:
      print(items,  end= ' ')
