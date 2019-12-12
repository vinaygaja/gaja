#Printing the 50 most frequently occurring words
#from collection module importing counter

from collections import Counter
#opening txt file and reading 
with open ("oliver Twist.txt") as FH:
    book=FH.read()
    spltbook=book.split(' ')

counter=Counter(spltbook)
kees=counter.keys()

#discarding words not required for given conditon

for key in list(counter):
    if key in kees:
        if len(key)<=4:
            del counter[key]
        elif key.startswith('h'):
            del counter[key]
        elif key.startswith('t'):
            del counter[key]
        elif key.startswith('w'):
            del counter[key]
        if key.startswith('y'):
            del counter[key]
#print(counter)
            
mostcount=counter.most_common(50)
print(mostcount)
        
        
    
