#Question:

##Modify program in S01Q02 to print the multiplication table 
##           of any number desired by the user

#Code:

#multiplication table of user desired number
c=1 
a=input("number desired by user?")
a=int(a)
#while c<11:
while c!=0:
    table=a*c
    print(table)
    c+=1

    
