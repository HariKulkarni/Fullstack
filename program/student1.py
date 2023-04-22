# student_enroll
c=int(input("enter 1 for enroll, 2 for retreive, 3 for delete, 4 to exit the loop"))

roll_no=[]
name=[]
age=[]
if c==1:
def enroll():
    # r=0 . it will fill details in first row
    r=0

    roll_no=int(input("Enter the Roll no :"))
    roll_no.append([r])
    name=input("Enter name  of the student")
    name.append([r])
    age=int(input("Enter the age of the student"))
    r=r+1
    # r=r+1, it will increment r to 2 and fill values in 2nd row, for 2nd student, in list r[1]

enroll()

elif c==2:
def retrieve():
# student_enroll
c=int(input("enter 1 for enroll, 2 for retreive, 3 for delete, 4 to exit the loop"))

roll_no=[]
name=[]
age=[]
if c==1:
def enroll():
    # r=0 . it will fill details in first row
    r=0

    roll_no=int(input("Enter the Roll no :"))
    roll_no.append([r])
    name=input("Enter name  of the student")
    name.append([r])
    age=int(input("Enter the age of the student"))
    r=r+1
    # r=r+1, it will increment r to 2 and fill values in 2nd row, for 2nd student, in list r[1]

enroll()

elif c==2:
def retrieve():
    # provide the roll no to see the details of the student
    # if r_no =5 , it will print the details from 4th row
    r_no=int(input("Enter the roll no to see the details of the student: "))
    print("roll no * name * age")
    print(roll_no[r_no-1],"*",name[r_no-1],"*",age[r_no-1]) 

retrieve()

elif c==3:
def deletedata():
    # provide the roll no to delete the details of the student
    r_no=int(input("Enter the roll no to delete the details of the student: "))
    del (roll_no[r_no-1],"*",name[r_no-1],"*",age[r_no-1]) 
    print("roll no * name * age")
    print(roll_no[r_no-1],"*",name[r_no-1],"*",age[r_no-1]) 

deletedata()    

elif c==4:
exit

else: 
    print("pls provide the correct option")
retrieve()

elif c==3:
def deletedata():
    # provide the roll no to delete the details of the student
    r_no=int(input("Enter the roll no to delete the details of the student: ")) 
    del (roll_no[r_no-1],"*",name[r_no-1],"*",age[r_no-1]) 
    print("roll no * name * age")
    print(roll_no[r_no-1],"*",name[r_no-1],"*",age[r_no-1]) 

deletedata()

elif c==4:
exit

else: 
    print("pls provide the correct option")