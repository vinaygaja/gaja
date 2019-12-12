dct=dict()
item=list()
#bill2=list()
#making txt file to dictionary
def bill_dct(FN):
    dct=dict()
    with open (FN) as FH:
        for line in FH:
            if ":" in line:
                if '0'in line:
                    if'.'in line:
                        a=line.split(':')
                        b=a[0].split('.')
                        n1=b[1].strip()
                        n2=a[1]
                        dct[n1]=[int(n2)]
        return(dct)
    
with open("bill.txt")as FH:
    for line in FH:
        
        if'TOTAL'in line:
            t=line.split(':')
            total=(t[1])
            #print('TOTAL:',total)
            
#list of item should be cancell
            
with open('items.txt') as FH:
    for line in FH:
        line1=line.split("\n")
        item.append(line1[0])
 #   print(item)

bill=bill_dct("bill.txt")
#print(bill)
for key in list(bill):
    if key in item:
        del bill[key]
#print(bill)
        
#printing new list of items in bill
        
c=0
for key in bill:
    c+=1
    print(c,key,end=':')
    for i in bill[key]:
        print(i,end='\n')

#collection of values

vlu=bill.values()
#print(vlu)

###calculating sum of values

sum=0
for i in vlu:
        sum=sum+int(str(i)[1:-1])
print("TOTAL:",sum)

#finding saved money

SA=int(total)-sum
print("Saved Money:",SA)



        
