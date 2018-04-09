import nltk
import sys
import string
import re
from nltk.tokenize import sent_tokenize
from nltk import *


patterns = [(r'.*uuru$','LOC'),(r'.*bhaT+','NAME'),(r'.*esh+','NAME'),
            (r'.*aLLi+','LOC'),(r'.*naanu$','None'),(r'.*goopi+','NAME'),
            (r'.*pura$','LOC'),(r'.*nnu+','NAME'),(r'.*singh+','NAME'),
            (r'.*nagara$','LOC'),(r'.*adha+','NAME'),
            (r'.*palya$','LOC'),(r'.*amma+','NAME'),
            (r'.*raL+','LOC'),(r'.*appa+','NAME'),
            (r'.*uuri+','LOC'),(r'.*aNNa+','NAME'),
            (r'.*magaDi+','LOC'),(r'.*akka+','NAME'),
            (r'.*alli$ ','LOC'),(r'.*gowDa+','NAME'),
            (r'.*gal+','LOC'),(r'.*kumaar+','NAME'),]


print('BEGIN\n')

f = open('krishna1.txt')
text = f.read()
f.close()


sent = nltk.word_tokenize(text)
for line in sent:

for i in chunked:
   if type(i) == Tree:
        current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue

    return continuous_chunk
    t = line.strip()
    pat = r'''(?x)([A-Z]\.)+| \w+(-\w+)*| \$?\d+(\.\d+)?%?| \.\.\.| [][.,;"'?():-_`]'''
    p = nltk.regexp_tokenize(t,pat)
    reg = nltk.RegexpTagger(patterns)
    #def stem(t):
    #for suffix in ['uuru','aLLi','pura','nagara','paLya','gaDi','alli','gal']:
    #regexp = [r'^(.*?)(uuru|aLLi|pura|nagara|paLya|gaDi|alli|gal)?$','LOC']
    #stem,suffix = re.findall(regexp,t)[0]
    #return (stem)

    pt = reg.tag(p)
    print(pt) 
print('\n')
print('Done')
    

