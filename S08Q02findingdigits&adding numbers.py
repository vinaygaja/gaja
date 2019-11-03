#Question:
##Ask the user to enter a number.
##- If the number is a single digit number, add 7 to it, 
##     and print the number in its unit’s place
##- If the number is a two digit number, raise the number to the power of 5, 
##     and print the last 2 digits
##- If the number is a three digit number, ask user to enter another number. 
##     Add the 2 numbers and print the last 3 digits

#Code:
#main starts from here:

num=input('enter a number:')
num=int(num)
if num>=0 and num<=9:
    num1=num+7
    print(num1%10)
elif num>=10 and num<=99:
    num2=(num**5)
    print(num2%100)
elif num>=100 and num<=999:
    n=input('enter another number:')
    n=int(n)
    num3=num+n
    print(num3%1000)
    

##Getting output:
## RESTART: C:/Users/Administrator/Desktop/pythonexercises/S08Q02findingdigits&adding numbers.py 
##enter a number:999
##enter another number:123
##122
##>>> 
## RESTART: C:/Users/Administrator/Desktop/pythonexercises/S08Q02findingdigits&adding numbers.py 
##enter a number:22
##32
##>>> 
## RESTART: C:/Users/Administrator/Desktop/pythonexercises/S08Q02findingdigits&adding numbers.py 
##enter a number:5
##2
