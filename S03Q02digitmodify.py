##Ask the user to enter a number.
##            - If the number is a single digit number,
##                 add 7 to it, and print the number in its unit’s place
##            - If the number is a two digit number,
##                raise the number to the power of 5, 
##                and print the number in its unit’s place
##            - If the number is a three digit number, 
##                ask the user to enter another number. 
##                Add the 2 numbers and print the number in its unit’s place
##
##            Use the solution provided in S03Q01 as the template for this exercises.
##            - Instead of doing a print to print the final result in "perform_check" function 
##            call separate functions : 
##               do_1digit_oper() and
##               do_2digit_oper() and
##               do_3digit_oper()
##            that will perform the required operations based on the number of digits.

#find 1 2 3 digit modify and print

#defining functions
def do_1digit_oper(num):
    return((num+7)%10)

def do_2digit_oper(num):
    return((num**5)%10)
def do_3digit_oper(num):
    n=input('enter num by user:')
    n=int(n)
    return((num+n)%10)

n=input('enter a numbers by user:')
num=n.split()
#c=0
for n in num:
    num=int(n)
    if num<10:
        d1=do_1digit_oper(num)
        print(d1)

    elif num>=10 and num<100:
        d2=do_2digit_oper(num)
        print(d2)
        
    elif num>=100 and num<1000:
        d3=do_3digit_oper(num)
        print(d3)
        
    
