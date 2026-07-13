print("====STUDENT SYSTEM====")
name=input("enter student name:")
mark=int(input("enter student mark:"))
print("name:",name)
print("mark:",mark)
if mark >= 90:
    print("grade: A")
    print("scholorship :100%")
elif mark >= 75:
    print("grade: B")    
    print("scholorship:50%")
elif mark >= 50:
    print("grade:C")
    print("scholorship:25%")
else :
    print("grade:F")
    print("no scholorship")  
print("thank you")       



