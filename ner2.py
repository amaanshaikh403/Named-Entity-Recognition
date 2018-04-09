import nltk
import sys
import re
import string

sent=[]
token=[]


text="""Natural language processing is a field of computer science,
    that deals with the building computers systems that will analyze,
    understand and generate natural language."""
#textfile = sys.argv[1]

#a = open("text.txt")
#text = nltk.word_tokenize( a.read() )# lowercase the text
#a.close()

print ('Begin')
#token=re.split(r' ', text)
token = nltk.word_tokenize(text)
sent=nltk.pos_tag(token)

print(sent)

print('done printing tokens with POS tag')



#grammar = "NP: {(((<DT>)*)<Name>((<IN>?<DT>?)*))+(((<DT>)*)<LOC>((<IN>?<DT>?)*))+(((<DT>)*)<ORG>((<IN>?<DT>?)*))+}"
grammar = "NP: {<DT>?<JJ>*<NN>}" 
cp = nltk.RegexpParser(grammar)
result = cp.parse(sent)
print (result)
result.draw()
    
print('DONE')



    
