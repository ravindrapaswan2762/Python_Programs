import re

mystr = '''Tata Limited
mo. no.- 9856235255
mo. no.- 98562-35255
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiin'''


# findall, search, split, sub, finditer



patt = re.compile(r'fass')             # find 'fass' charecter
#patt = re.compile(r'.admi')            # . any character in the place of 'dout(.)'
#patt = re.compile(r'^Tata')            # start with Tata
#patt = re.compile(r'iin$')              # end win iin
#patt = re.compile(r'ai{2}')              # two times of i with a
#patt = re.compile(r'(ai){2}')            # two time of ia
#patt = re.compile(r'ai{1}|Fax')         # one time i with a or Fax
#patt = re.compile(r".{4}mi")            # previous 4 character of 'mi'

# Special Sequences
#patt = re.compile(r'\ATata')            # who word which is start with Tata
#patt = re.compile(r'\bFax')              # who word which is start with Fax
#patt = re.compile(r'Fax\b')              # who word which is start with Fax
#patt = re.compile(r'27\b')              ## who int which is start with 27
patt = re.compile(r'\d{5}-\d{4}')
patt = re.compile(r'\d{5}-\d{5}')        # d for digits
# Task
# Given a string with a lot of indian phone numbers starting from +91
matches = patt.finditer(mystr)
for match in matches:
    print(match)
