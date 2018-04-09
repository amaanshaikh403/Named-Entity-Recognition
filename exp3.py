import nltk
import sys
import string
import re
from nltk.tokenize import sent_tokenize

from nltk import *

patterns = [(r'.*uuru$','LOC'),(r'.*bhaT+','NAME'),(r'.*sh+','NAME'),
            (r'.*aLLi+','LOC'),(r'.*naanu$','None'),(r'.*goopi+','NAME'),
            (r'.*pura$','LOC'),(r'.*anu+','NAME'),(r'.* singh+','NAME'),
            (r'.*nagara$','LOC'),(r'.*adha+','NAME'),
            (r'.*palya$','LOC'),(r'.*amma+','NAME'),
            (r'.*raL+','LOC'),(r'.*appa+','NAME'),
            (r'.*uuri+','LOC'),(r'.*aNNa+','NAME'),
            (r'.*gaDi+','LOC'),(r'.*akka+','NAME'),
            (r'.*alli$ ','LOC'),
            (r'.*gal+','LOC'),(r'.* kumar+','NAME'),]

#text="""hi maisuuru"""

textfile = sys.argv[1]

a = open(textfile)
text = nltk.word_tokenize( a.read() )# lowercase the text
a.close()
reg = nltk.RegexpTagger(patterns)
p = reg.tag( text )
print(p)

