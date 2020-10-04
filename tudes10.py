# DICTIONARY IS NOTHING BUT KEY VALUE PAIRS
"""d1 = { }
print(type(d1))"""
d2 = {"harry":"burger", "ravindra":{"mornning":"samosa", "noon":"daal,rice", "evening":"daal,roti"}, "rohan":"fish", "mohan":"roti"}
print(d2)
print(d2["ravindra"] )

#d2["ankit"] = "junk food"                 # for adding new value
#print(d2)
      #OR
d2.update({"mohan":"toffee"})
print(d2)

#print(d2.items())

#print(d2.keys())

#del d2["mohan"]                           # for remove some value or persion

