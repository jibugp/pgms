
file = open("Students.txt", "w")
file.write("Student Name : J \nAge : 27 \nCourse : python")
file.close()

file = open("Students.txt", "r")
data = file.read()
print(data)
file.close()

file = open("Students.txt", "a")
file.write("\nMark : 100")
file.close()

file = open("Students.txt", "r")
data = file.read()
print(data)
file.close()
