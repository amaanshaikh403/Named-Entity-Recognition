import sys
import string
import re

# command line arguments
#dictfile = sys.argv[1]
#textfile = sys.argv[2]

a = open("krishna2.txt")
text = str.split( a.read() ) # lowercase the text
a.close()

a = open("location.txt")
lines = a.readlines()
a.close()

dic = {}
scores = {}

# a default category for simple word lists
current_category = "Location"
scores[current_category] = 0

# inhale the dictionary
for line in lines:
    if line[0:2] == '>>':
        current_category = str.strip( line[2:] )#Return a copy of the string with the leading and trailing characters removed.
        scores[current_category] = 0
    else:
        line = line.strip()
        if len(line) > 0:
            pattern = re.compile(line, re.IGNORECASE)
            dic[pattern] = current_category
            
# examine the text
for token in text:
    for pattern in dic.keys():
        if pattern.match( token ):
            categ = dic[pattern]
            print (categ, ":", token)
            scores[categ] = scores[categ] + 1

for key in scores.keys():
    print (key, ":", scores[key])
