my_file=open("student.txt","w")

print(my_file.write(input("enter the student Id :\n")))
print(my_file.write(input("enter the student Name :\n")))
print(my_file.write(input("enter the student course :\n")))


my_file=open("student.txt","r")
print(my_file.read())