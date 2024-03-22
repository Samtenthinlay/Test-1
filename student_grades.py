num_student = int(input("Enter the number of student: "))
i = 1
while i <= num_student:
    total_grade=0
    num_subject = int(input(f"Enter the number of subject for student {i}:")) 

    for j in range(1,num_subject +1):
        grade = float(input(f"Enter subject{j} grade for stuudent {i}:"))
        total_grade += grade
    
    average_grade = total_grade/ num_subject
    print(f"Average grade for student {i}: {average_grade: .2f} ")
    i += 1