#sowmi5
x,y=map(int,raw_input().split())
for num in range(x+1,y):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print num,
# primeinterval.com
