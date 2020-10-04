f1 = open("ravindra_add.txt")


try:
    f = open("ravindra_return.txt")

except Exception as e:
    print(e)

else:
    print("This will run only, if except is not running")

finally:
    print("run this anyway...")
    f1.close()

print("important stuff")