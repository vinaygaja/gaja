#calculating milage of car

#from calci import sub,div

sv=input("starting reading:")
sv=int(sv)                             
ev=input("ending reading:")
ev=int(ev)
fltr=input("fuel consume:")
fltr=int(fltr)

#from calci import sub
#vrun=sub(ev,sv)
vrun=ev-sv
print(vrun)
#from calci import div
#milage=div(vrun,fltr)
milage=vrun/fltr
print (milage)
