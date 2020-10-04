"""
import time
def searcher():
    import time
    # some 4 seconds time consuming task
    book = "this is a book on ravindra , god bless you"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Your text is not in the book")

search = searcher()
print("Searching.......")
next(search)        #next method jaise hi run hota hai wo time module me chala jata hai#
print("next method run....")
time.sleep(3)
search.send("ravindra")
input("press any key : ")
search.send("ravindra")
"""
##########################################
import time


def searcher():
    # some 4 seconds time consuming task
    book = "ravindra, harry, mohan, bheem, raju, jaggu, chuttki, dholu, bholu, kaliya, indumati"
    time.sleep(4)

    while True:

        text = (yield)
        if text in book:
            print("Your name is in the book")
        else:
            print("Your name is not in the book")

        print(text)

search = searcher()
print("Searching.......")
next(search)
search.send("bheem")






