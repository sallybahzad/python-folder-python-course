number=int (input("enter a 3 digit number"))
sum=0
temp=number
while temp>0:
    digit= temp%10
    sum+=digit**3
    temp //=10
    print(temp)
    if number==sum:
        print("number is an armstrong number.", number)
    else:
        print("number is not an armstrong number.",number)






































