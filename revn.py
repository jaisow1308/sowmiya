a=int(input("Enter number: "))
r=0
while(a>0):
    dig=a%10
    r=r*10+dig
    a=a//10
print("Reverse:",r)
