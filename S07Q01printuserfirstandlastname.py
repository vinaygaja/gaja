#Question:
    
##Get the user’s first name and last name. 
##        Assume the user provides “Dharmender” and “Singh” as inputs, 
##          then print the user’s name in the following order and format
##
##        - Name : dharmender, Surname : singh 
##        - DHARMENDER SINGH
##          ---------------------  ---------
##        - Singh, Dharmender

#code:

#print the user first name and last name

fname=input("what is your name:")
sname=input("what is your surname:")

print(fname,sname)

print ('Name:',fname.lower(),',Surname:',sname.lower())

print(fname.upper(),sname.upper())
print('----------- -----')
print(sname,',',fname)

#getting output:

## RESTART: C:\Users\Administrator\Desktop\pythonexercises\S07Q01printuserfirstandlastname.py 
##what is your name:Dharmrnder
##what is your surname:Singh
##Dharmrnder Singh
##Name: dharmrnder ,Surname: singh
##DHARMRNDER SINGH
##----------- -----
##Singh , Dharmrnder
