#multiplication of user desired number by function

def mul(num1,num2):
    res=num1*num2
    return(res)

c=1 
a=input("number desired by user?")
a=int(a)
while c<11:
    table=mul(a,c)
    print(table)
    c+=1
