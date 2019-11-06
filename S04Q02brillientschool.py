#brillient school exam

maxeng=80
maxsci=90
maxmaths=100
tmm=80+90+100

sse=input("student scored in english:")
sse=int(sse)
sss=input('student scored in science:')
sss=int(sss)
ssm=input('student scored in maths:')
ssm=int(ssm)

tms=sse+sss+ssm
sp=((tms/tmm)*100)

if sp>=90:
    print('first class')

elif sp>=75:
    print('second class')

elif sp<=35:
    print('failed')
    
else:
    print('average')
    
