import nltk
from nltk.tokenize import sent_tokenize
import sys
import string
import re
import string
from nltk import *

# command line arguments

a = open('krishna2.txt')
text = str.split( a.read() ) # lowercase the text
a.close()

a = open('location.txt')
lines = a.readlines()
a.close()

dic = {}
scores = {}


patterns = [(r'.*uuru$','LOC'),(r'.*bhaT+','NAME'),(r'.*esh+','NAME'),
            (r'.*aLLi+','LOC'),(r'.*naanu$','None'),(r'.*goopi+','NAME'),
            (r'.*pura$','LOC'),(r'.*singh+','NAME'),
            (r'.*nagara$','LOC'),(r'.*anu+','NAME'),
            (r'.*palya$','LOC'),(r'.*amma+','NAME'),
            (r'.*raL+','LOC'),(r'.*appa+','NAME'),
            (r'.*uuri+','LOC'),(r'.*aNNa+','NAME'),
            (r'.*magaDi+','LOC'),(r'.*akka+','NAME'),
            (r'.*alli$ ','LOC'),(r'.*gowDa+','NAME'),
            (r'.*gal+','LOC'),(r'.*kumaar+','NAME'),]


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
            #categ = dic[pattern]
            #for line1 in categ:
                #t = line1.strip()
                #pat = r'''(?x)([A-Z]\.)+| \w+(-\w+)*| \$?\d+(\.\d+)?%?| \.\.\.| [][.,;"'?():-_`]'''
            p = nltk.regexp_tokenize(line,pattern)
            reg = nltk.RegexpTagger(patterns)
            #pt = reg.tag()
            dic[reg] = current_category

# examine the text
for token in text:
    for pattern in dic.keys():
        if pattern.match( token ):
            #categ = dic[pattern]
            #for line1 in categ:
                #t = line1.strip()
                #pat = r'''(?x)([A-Z]\.)+| \w+(-\w+)*| \$?\d+(\.\d+)?%?| \.\.\.| [][.,;"'?():-_`]'''
                #p = nltk.regexp_tokenize(t,pat)
                #reg = nltk.RegexpTagger(patterns)
                #pt = reg.tag()
                categ = dic[pattern]

                print (categ, ":", token)
                scores[categ] = scores[categ] + 1

                for key in scores.keys():
                    print (key, ":", scores[key])





#print('BEGIN\n')


#sent = nltk.word_tokenize(text)
    #def stem(t):
    #for suffix in ['uuru','aLLi','pura','nagara','paLya','gaDi','alli','gal']:
    #regexp = [r'^(.*?)(uuru|aLLi|pura|nagara|paLya|gaDi|alli|gal)?$','LOC']
    #stem,suffix = re.findall(regexp,t)[0]
    #return (stem)

    
