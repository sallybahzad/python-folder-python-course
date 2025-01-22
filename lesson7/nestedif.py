medical_cause=input("did you have a medical cause? yes/no")
attendance=int(input("enter the attendance of the student."))
if medical_cause =="yes":
    print("you are allowed.")
else:
    if attendance >= 75:
        print("allowed")
    else:
        print("not allowed")
        
    

 
