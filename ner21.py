import nltk
from nltk import *
import sys
import re
import string



patterns = [(r'.*uuru$','LOC'),
            (r'.*aLLi+','LOC'),
            (r'.*pura$','LOC'),
            (r'.*nagara$','LOC'),
            (r'.*palya$','LOC'),
            (r'.*raL+','LOC'),
            (r'.*uuri+','LOC'),
            (r'.*gaDi+','LOC'),
            (r'.*alli$ ','LOC')]


textfile = sys.argv[1]

a = open(textfile)
text = nltk.word_tokenize( a.read() )# lowercase the text
a.close()

print ('Begin')



reg = nltk.RegexpTagger(patterns)
p = reg.tag(text)
t = str.split(p)
print (t)

    
print('DONE')



    
