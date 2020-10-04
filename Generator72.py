"""
itrable - jisme    __iter__() or __gettime__()   type waala method difine hota hai
itrator - jisme   __next__()    type  wala function define hota hai,
itration - itrate karne ki prakriya hoti hai, ye ek tarah ke itrator hota hai,
generator -   ye live value ko generate karta hai, na
            ki store karke rakhta hai
"""
# for examle:-
def gen(n):
    for i in range(n):
        yield i          #yield a type of a generator

g = gen(445)
print(g)
#####################
def gen(n):
    for i in range(n):
        yield i

g = gen(10)
#print(g)
"""print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())"""
  # OR #
for i in g:
    #print(g.__next__())
       # OR #
    print(i, end=" ")
##################################

h = "RAVINDRA"  ### string bhi itrator hote hai ###
#ite = iter(h)
#print(h.__next__())
"""print(ite.__next__())
print(ite.__next__())
print(ite.__next__())
print(ite.__next__())
print(ite.__next__())
print(ite.__next__())
print(ite.__next__())"""





