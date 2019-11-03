#miniproject 1
number=range(1,25)
loginnum=input('assume number:')
loginnum=int(loginnum)
lch=0
while lch<5:
    passcode=input('guess the number:')
    passcode=int(passcode)
    if passcode < loginnum-2:
        print("invalid passcode")
    elif passcode>loginnum+2:
        print("INVALLID PASSCODE")
    elif passcode >= loginnum-2 and passcode < loginnum:
        print("InVaLiD PaSsCoDe")
    elif passcode>loginnum and passcode<=loginnum+2:
        print("InVaLiD PaSsCoDe")
    elif passcode==loginnum:
        print("welcome")
    lch+=1
    
