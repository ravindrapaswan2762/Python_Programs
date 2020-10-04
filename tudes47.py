list = ["john", "cena", "randy", "orton", "shemus", "khali", "jinder mahal"]
for item in list:
    print(item, "and", end=" ")


### OR ###

a = " , ".join(list)
print(a)