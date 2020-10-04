
"""f = open("ravindra.txt", "rt")
content = f.read()
print(content)

f.close()"""

  ### OR ###

"""f = open("ravindra.txt", "rt")
for line in f:
    print(line, end=" ")
f.close()"""

   ## OR ###
"""f = open("ravindra.txt", "rt")
print(f.readline())
print(f.readline())
print(f.readline())"""
  ### OR ###
f = open("ravindra.txt", "rt")
print(f.readlines())


"""f = open("ravindra3.txt", "r")
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(0)
f.close()"""