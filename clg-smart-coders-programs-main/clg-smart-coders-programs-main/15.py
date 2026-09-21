# count bits
n=int(input("enter a no: "))
count=0

while n>0:
    n= n&(n-1)
    n+=1
    print (n)