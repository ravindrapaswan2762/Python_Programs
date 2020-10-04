class dad:
    basketball = 1

class son(dad):
    dance = 1
    def isdance(self):
        return f"yes i dance {self.dance} no of time "

class granson(son):
    dance = 6
    def isdance(self):
        return f"jacjkson yeah!" \
            f"yes i dance very awesomely {self.dance} no of time "

darry = dad()
larry = son()
harry = granson()

print(harry.basketball)
print(harry.isdance())


#### H.W ##
#  make a project with electronic device, pocket gadget, phone as a multiple inheritense...

