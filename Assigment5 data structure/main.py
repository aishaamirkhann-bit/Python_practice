import college

student_list = ["Aisha","Gully","Aiman","Areeba", "Adan"]    

print(college.Welcome())
print(college.display_students(student_list))
print(college.total_students(student_list))


# list
student=["Aisha","Gully","Aiman","Areeba", "Adan"]
print("Student List = ",student)
print(len(student))

student.append("Ansa")
print("Updated Student List = ", student)

student.remove("Aiman")
print("Updated Student List after removing Aiman = ", student)

student[2] = "Asma"
print("Updated Student List after changing Areeba to Asma = ", student)

print("Total number of students = ", student)

# tuples

information=("Roll Number","Department","Semester")
print(information[0])
print(information[1])
print(information[2])

# error explanation becasue in tuples data canot be modify

# set

club={"Sports","Drama","Sports","Debate", "Cricket", "Drama"}
print(club)
club.add("Music")
print(club)
club.remove("Debate")
print(club)

if "Drama" in club:
    print("Drama Club is present")
else:   
    print("Drama Club is not present") 

