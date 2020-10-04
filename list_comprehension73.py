ls = []
for i in range(100):
    if i%3==0:
        ls.append(i)
print(ls)

####  OR ###########
ls = [i for i in range(100) if i%3==0]   # this list comprehension, sirf ek line me likhna
print(ls)
#############################################################################################

dict1 = {i:f"item {i}" for i in range(100)}
dict2 = {value:key for key,value in dict1.items()}  # for reverse
print(dict1,"\n", dict2)

######################################## list and dict. comprehension ############################################
dresses = {dress for dress in ["dress1", "dress2", "dress1", "dress2", "dress1", "dress2"]}
print(dresses)
print(type(dresses))

dresses = [dress for dress in ["dress1", "dress2", "dress1", "dress2", "dress1", "dress2"]]
print(dresses)
print(type(dresses))
###################################### generator comprehension #################################################
even = (i for i in range(100) if i%2==0)
print(even.__next__())
print(type(even))
# or #
for item in even:
    print(item, end=" ")



