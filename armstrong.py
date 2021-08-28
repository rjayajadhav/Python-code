n=int(input("enter the no"))
sum=0
temp=n
while (temp>0):
    rem=temp%10
    sum +=rem**3
    temp//=10 

if (temp==sum):
        print("no is armstrong")
else:
        print("no is not armstrong")

     