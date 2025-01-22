print("select your ride")
print("1.bike")
print("2.car")
choice=int(input("enter your choice: "))
if choice==1:
    print("what type of bike?")
    print("1.scooty\n")
    print("2.scooter\n")
    choice2=int(input("enter your choice 2: "))
    if choice2==1:
        print("you have selected scooty")
    else:
        print("you have seleced scooter")
elif choice==2:
    print("what type of car?")
    print("1.sedan")
    print("2.XUV")
    choice3=int(input("enter your choice 3: "))
    if choice3==1:
        print("you have selcted sedan")
    else:
        print("you have selected XUV")
else:
    print("wrong choice")
    
        




      