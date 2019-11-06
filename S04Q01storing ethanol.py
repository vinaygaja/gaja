#storing ethanol

ttc=900
cl=input("enter current level oftank :")
cl=int(cl)
cll=(ttc//100)*cl
if cll>=((ttc//100)*80):
    print("close the valve")
elif cll<=((ttc//100)*20):
    print("by more liquid")
else:
    print()
