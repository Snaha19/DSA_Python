class student:
    def __init__(self,name,roll,marks):
        self.name= name
        self.roll=roll
        self.marks=marks

    def display_details(self):
            print(self.name)
            print(self.roll)

    def calculate_grade(self):
         
         if self.marks>=90:
              return 'A'
         elif self.marks>=75:
              return 'B'
         elif self.marks>=50:
              return 'C'
         else:
                return 'F'
         
         
         
name=input("Enter the name of the student: ")
roll=int(input("enter the roll of the student : "))
marks=int(input("enter marks of the student :"))


s1=student(name,roll,marks)
s1.display_details()
grade=s1.calculate_grade()
print(grade)

name=input("Enter the name of the student: ")
roll=int(input("enter the roll of the student : "))
marks=int(input("enter marks of the student :"))

s2=student(name,roll,marks)
s2.display_details()
grade=s2.calculate_grade()
print(grade)

name=input("Enter the name of the student: ")
roll=int(input("enter the roll of the student : "))
marks=int(input("enter marks of the student :"))

s3=student(name,roll,marks)
s3.display_details()
grade=s3.calculate_grade()
print(grade)