#qUESTION:

##Write a search and replace program in Python. 
##This should first take the original text as input by prompting the user for it. 
##It should then, prompt the user for which word to search, 
##and what new word it should be replaced with.

#Code:

#search and replace word

ex=input('enter text by user:')
fw=input('enter word to find:')
rw=input('enter word which to insert:')

#main starts here
print("original sentence:",ex)
w=ex.find(fw)
#print(w)
rep=ex.replace(fw,rw)
print("Replaced sentence:",rep)

#Getting Output :

## RESTART: C:/Users/Administrator/AppData/Local/Programs/Python/Python37-32/S09Q02searchandreplaceprogram.py 
##enter text by user:banglore is cool

##enter word to find:cool

##enter word which to insert:hot

##original sentence: banglore is cool

##Replaced sentence: banglore is hot
