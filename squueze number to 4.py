n=int(input())
c=1
s=0
x=n
if n<=4 and n>1000000000:
    print('no')
else:
    while c<=10:
        while x>0:
            k=x%10
            s=s+k*k
            x=x//10 
        if s==4:
            print(c)
            break
        else:
            c=c+1
            x=s
            s=0
            