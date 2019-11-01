#Question:

##Get the user’s first name and last name. 
##        Assume the user provides “Dharmender” and “Singh” as inputs, 
##        Find his best possible initials by eliminating the last character 
##        from each of the name as shown in this sample output
##
##        - Step 1 : Dharmender Singh
##        - Step 2 : Dharmende Sing
##        - Step 3 : Dharmend Sin
##        - Step 4 : Dharmen Si
##        - Step 5 : Dharme S
##
##        Expected output :
##        Best possible initials of "Dharmender Singh" is :
##        Dharme S

#Code:

#print the user first name and last name

fname=input("what is your name:")
sname=input("what is your surname:")

##print(fname,sname)
##print(fname[:-1],sname[:-1])
##print(fname[:-2],sname[:-2])
##print(fname[:-3],sname[:-3])


print('Best possible initials of "Dharmender Singh" is :',fname[:-4],sname[:-4])


##output:
##
##    
##RESTART: C:\Users\Administrator\Desktop\pythonexercises\S07Q02possibleinitials.py 
##what is your name:Dharmender
##what is your surname:Singh
##Best possible initials of "Dharmender Singh" is : Dharme S
