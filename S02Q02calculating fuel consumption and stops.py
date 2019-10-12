#calculating fuel consumption and stops to refilling#calculating milage of car

#from calci import sub,div

sv=input("starting reading:")
sv=int(sv)                             
ev=input("ending reading:")
ev=int(ev)
carmilage=input("car milage:")
carmilage=int(carmilage)

#from calci import sub
#vrun=sub(ev,sv)
vrun=ev-sv
print(vrun)
#from calci import div
#fuelconsume=div(vrun,carmilage)
fuelconsume=vrun/carmilage
print (fuelconsume)
#calculate stops to refiling
#from calci import div
btog=input("distance:")
btog=int(btog)
#fuelrequire=div(btog,carmilage)
fuelrequire=btog/carmilage
print (fuelrequire)
tc=input("tank capacity:")
tc=int(tc)
#print(tc)
#stops=div(fuelrequire,tc)
stops=fuelrequire/tc
print(round(stops))
