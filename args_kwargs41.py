"""def funargs(*args):
    for item in args:
        print(item)

har = ["harry", "rohan", "mohan", "sohamn", "add more value"]
funargs(har)"""


def funargs(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)

    for key, value in kw.items():
        print(f" {key} is a {value}")

print("\n now i would like to introduce some of our houbies")


har = ["harry", "rohan", "mohan", "sohamn",]
normal = " i am a normal argument and the student are : "

kw = {"harry":"programmer", "mohan":"fitness", "rohan":"instructor", "sohan":"player"}
funargs(normal, *har, **kw)






