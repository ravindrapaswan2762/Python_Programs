def take(k):
    if(k == 1):
      ls = input("what type of your item plz enter 1 \n : ")
      for item in ls:
            print(item)

    if(k == 2):
        ls = input("what type of your item plz enter\n : ")
        for item in ls:
           print(ls)
    else:
        print("You entered wrong value ")
def retrieve(k):
    if(k == 1):
        dict1 = input("What type of your otem plz enter\n : ")
        for i in dict1:
            print(dict1)

    if (k == 2):
        dict1 = input("What type of your otem plz enter\n : ")
        for i in dict1:
            print(dict1)
    else:
        print("You entered wrong value ")


a = input("What type of your comprehension, LIST for 1 and SET for 2 : ")
if(a == 1):
    print("What is the no of your item : ")
    take(a)
else:
    print("What is the no of your item : ")
    retrieve(a)