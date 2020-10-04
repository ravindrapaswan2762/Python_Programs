"""print("enter your number ")
impnum = input()
print("you entered ", impnum)
print("you entered", int(impnum)+10)"""


#NEW TOPIC
mystr = "ravindra is a good boy"
#print(mystr.endswith("boy"))

#print(mystr[0:5])             #>>>> zero possition is included but 5 possition is not included, in this presence all type str are printed
#print(mystr[0::5])           #if starting ratio empty then take automatic zere, if end ratio empty then take zero or all str print
#print(mystr[::-1])           #   [::]==[x:x:x]
#print(mystr[::2])
#print(mystr[14:18:])

#print(mystr.isalpha())
#print(mystr.isalnum())
print(mystr.endswith("boy"))
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.find("d"))
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("is","are"))
