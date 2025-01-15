a=int(input("enter a value"))
b=int(input("enter a value 2"))
c=int(input("enter a value 3"))
avg=(a+b+c)/3
print("avg=", avg)
if avg > a or avg > b or avg > c:
    print("%d is higher than %d, %d,%d" %(avg,a,b,c))

