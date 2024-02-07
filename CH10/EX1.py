GRADES = input("Eneter scores : ")
grades_list = GRADES.split()
int_grades = [eval(x) for x in grades_list]
int_grades.sort()

for grade in int_grades :
    if grade >= int_grades[len(int_grades)-1] - 10:
        print("Student "+str(int_grades.index(grade))+" score is " +str(grade)+" and grade is A")
    elif grade >= int_grades[len(int_grades)-1] - 20:
        print("Student "+str(int_grades.index(grade))+" score is " +str(grade)+" and grade is B")
    elif grade >= int_grades[len(int_grades)-1] - 30:
        print("Student "+str(int_grades.index(grade))+" score is " +str(grade)+" and grade is C") 
    elif grade >= int_grades[len(int_grades)-1] - 40:
        print("Student "+str(int_grades.index(grade))+" score is " +str(grade)+" and grade is D")
    else:
        print("Student "+str(int_grades.index(grade))+" score is " +str(grade)+" and grade is F")
