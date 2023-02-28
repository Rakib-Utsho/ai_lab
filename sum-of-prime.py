low = int(input("Enter The Lower limit: "))
up = int(input("Enter The Upper Limit: "))
sum = 0
for num in range(low,up+1):
    for i in range(2,num):
        if(num%i==0):
            break;
    else:
        print(num,"Is Prime Number")
        sum=sum+num
print("Sum of Prime Number is", "=", sum)