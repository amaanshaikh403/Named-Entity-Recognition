import loc
import stop
import nltk
import sys
import string
import re
from nltk.tokenize import sent_tokenize
from nltk import *
from nltk.corpus import stopwords
print('BEGIN\n')

#text = stop.stop_words_removal()
f=open("krishna.txt")
line = f.read()
f.close()

scores ={}
last_letters = 0
#sent = nltk.word_tokenize(line)
for lines in line:
        if lines.strip() == '.':
            text = nltk.word_tokenize(lines)
            print("\n")
            
            

        key = [r'^(.*?)(uuru|aLLi|pura|nagara|paLya|gaDi|alli|gal)?$','LOC']
        















#regexp = [r'^(.*?)(uuru|aLLi|pura|nagara|paLya|gaDi|alli|gal)?$','LOC']
#STOP_TYPES = ['naanu','neenu','avanu','.',',']
#sent = nltk.word_tokenize(line)
#for w in line:
 #   chunked = nltk.chunk(w)
   # print (chunked)
  #            
#print (sent)
#   lines = set (('naanu','.',',','avanu'))
 #   stop = set(stopwords) - lines
        
  #  print (t1)
   # pat = r'''(?x)([A-Z]\.)+| \w+(-\w+)*| \$?\d+(\.\d+)?%?| \.\.\.| [][.,;"'?():-_`]'''
    #pat1 = join(stopwords.words(pat))
    #pattern = nltk.regexp_tokenize(t,pat1)
    #patterns = loc.stem(pattern)
    #reg = nltk.RegexpTagger(patterns)
    #pt = reg.tag(p)
    #print(pt) #
#print('\n')
#print('Done')



    

