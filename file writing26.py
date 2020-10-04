
f = open("ravindra.txt", "w")                                # this mode is remove previous content and add new content
print(f.tell())                         #>>> knowing for where is file pointer in any file
#print(f.seek())                          #>>> use for return reset the file pointer
f.write("next ion man is coming soon from plamuuuuu...\n")
print(f.tell())
f.close()

#### OR  ###

"""f = open("ravindra.txt", "a")                                #  apend mode fore addind new content
b = f.write("where thanos will nothing front of me...\n")          # more time run, more copy content from append mode
print(b)   #>>> for how many new character print
f.close()"""


"""f = open("ravindra.txt", "r+")                                                 #  r+ mode use for writing and reading both mode
f.write("ravindra have both of power(ionman and thanos) now... \n")
f.write("thank you...")
f.close"""







