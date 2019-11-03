#calculating milage of car using function
#define functions

def add(num1,num2):
    res=num1+num2
    return res

def sub(num1,num2):
    res=num1-num2
    return res
def div(num1,num2):
    res=num1/num2
    return res

#starts here

sv=input("starting reading:")
sv=int(sv)                             
ev=input("ending reading:")
ev=int(ev)
fltr=input("fuel consume:")
fltr=int(fltr)

#using functions
vrun=sub(ev,sv)
#vrun=ev-sv
print(vrun)
#using function
milage=div(vrun,fltr)
#milage=vrun/fltr
print (milage)
