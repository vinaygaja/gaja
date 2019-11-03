#first 12 even fibonacci numbers
a=1
b=1
c=0
i=34
while c<i:
    fb=a+b
    b=a
    a=fb
    if fb%2==0:
        print(fb)

    c+=1
