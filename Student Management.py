class Student:
    def __init__(self,student_id,name,department,is_enrolled):
        self.__student_id=student_id
        self.__name=name
        self.__department=department
        self.__is_enrolled=is_enrolled
    def enroll_student(self):
        if self.__is_enrolled:
            print('The student is already enrolled')
        else:
            self.__is_enrolled=True
    def drop_student(self):
        if  not self.__is_enrolled:
            print('The Student is already dropped')
        else:
            self.__is_enrolled=False
            print('The student dropped successfully')
    def view_student_info(self):
        print('Name : ',self.__name)
        print('ID : ',self.__student_id)
        print('Department : ',self.__department)
        print('Enrollment Status : ',self.__is_enrolled)
    @property
    def student_id(self):
        return self.__student_id
    



class StudentDatabase:
    student_list=[]
    @classmethod
    def add_student(self,st):
        self.student_list.append(st)
    @classmethod
    def get_students(self):
        return self.student_list





s1=Student(101,'Mahir','CSE',True)
s2=Student(102,'Rahim','EEE',False)
s3=Student(103,'Karim','BBA',True)

StudentDatabase.add_student(s1)
StudentDatabase.add_student(s2)
StudentDatabase.add_student(s3)





while True:
    print("\n===== Student Management System =====")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input("Enter your choice: ")




    if choice == "1":
        students = StudentDatabase.get_students()
        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                student.view_student_info()
    





    elif choice == "2":
        sid = int(input("Enter Student ID to enroll: "))
        found = False
        for student in StudentDatabase.get_students():
            if student.student_id==sid:
                student.enroll_student()
                found = True
                break
        if not found:
            print("Invalid Student ID.")





    elif choice == "3":
        sid = int(input("Enter Student ID to drop: "))
        found = False
        for student in StudentDatabase.get_students():
            if student.student_id==sid:
                student.drop_student()
                found = True
                break
        if not found:
            print("Invalid Student ID.")






    elif choice == "4":
        print("Exiting program...")
        break





    else:
        print("Invalid choice. Please try again.")