
num=int(input("Enter a number: "))
n=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**n
    temp//=10
if num==sum:
    print("It is an Armstrong Number")
else:
    print("It is not an Armstrong Number")
