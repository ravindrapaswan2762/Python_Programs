# email collector
import re



mystr = '''
SUPPORT ME PLEASE



[[ 95% OFF JUST FOR YOU ]]

email = admin@123gmail.com
email = admin124@gmail.com
email = admin125@gmail.com
email = admin125@gmail.com


Hi Beautiful People out there
Hope you are doing great

Here i am giving some special DISCOUNT for my BESTSELLING website Design courses for you

Its Actual Price is 200 usd But i am giving to you just in 10 usd Just 95% OFF for being my YouTube Family


Courses Are following

====================================================

Phostoshop To Parallax Responsive Website design



-------------------------'''

# \w+@\S+\w
"""

list1=re.findall(r'\w+@\w+\S+',mystr)
      #  OR  #
#list1=re.findall(r'\w+@\S+',mystr)

op = open("email_store.txt","a")

j=1
for item in list1:
    op.write(f"Email{j}:{item}\n")
    j=j+1
op.close()
 
print(f"Email's are:{list1}")
print(f"Total Email's are:{j-1}")"""
#############################################
list2 = re.findall(r'\w+@\S+', mystr)
op = open("email.txt", "a")
j = 1
for item in list2:
    op.write(f"Email{j}:{item}\n")
    j=j+1
op.close()
print(f"emails are: {list2}")
print(f"total no of email : {j}")