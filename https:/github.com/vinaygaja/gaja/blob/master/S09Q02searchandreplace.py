    #find 1 2 3 digit modify and print
#num=input('enter a number:')
n=input('enter a numbers by user:')
num=n.split()
#c=0
for n in num:
    num=int(n)
    if num<10:
    #do_1digit_opr(num)
        print((num+7)%10)

    elif num>=10 and num<100:
    #do_2digit_opr(num)
        print((num**5)%10)
        
    elif num>=100 and num<1000:
    #do_3digit_(num)
        n=input('enter num by user:')
        n=int(n)
        print((num+n)%10)
        #c+=1
    
#callfunctions
        #do_1digit_oper()and
        #do_2digit_oper()and
        #do_3digit_oper()
