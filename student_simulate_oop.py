# student report card generator

"""Build a system that collects student data and subject-wise marks to generate a report card.
- Include grade calculation, average score, and pass/fail result.
- Use encapsulation for mark storage and method abstraction for result generation."""

class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.__marks = {}

    def get_marks(self):
        return self.__marks

    def add_marks(self, **subject):
        for sub, marks in subject.items():
            self.__marks[sub] = marks

    def calculate_average_score(self):
        total = sum(self.__marks.values())
        average = total / len(self.__marks)
        return average

    def is_passed(self):
        has_passed = all(mark >= 35 for mark in self.__marks.values())
        if has_passed:
            print(f"{self.name} is passed ")

        else:
            print(f"{self.name} is failed")

        return has_passed

    def calculate_grade(self):
        if self.is_passed():
            persentage = self.calculate_average_score()
            if persentage >= 90:
                 print(f"{self.name} is passed with grade 'A+'")

            elif persentage >= 80:
                 print(f"{self.name} is pased with grade 'A'")

            elif persentage >=70:
                 print(f"{self.name} is passed with grade 'B+'")

            elif persentage >=35:
                print(f"{self.name} is passed with grade 'B'")

            else :
                print(f"{self.name} is failed with grade'C'")

class ReportCard:

    def generate(self, student: Student):
        student_marks = student.get_marks()
        print("=============marks===============")
        print(f"\nRoll Number: {student.roll_no}  --  Name: {student.name}\n")
        for subject in student_marks.items():
            print(f"---{subject}")
            #print("________________________________")

        total = sum(student_marks.values())
        print("------------------------------------")
        print(f"total: {total}")

        print("==================================")
        print(f"Average : {student.calculate_average_score():.2f}")
        #student.is_passed()
        student.calculate_grade()

    def generate_all(self,students):
        for student in students:
            self.generate(student)

class  Classroom:
    def __init__(self, grade, section):
        self.grade = grade
        self.section = section
        self.__students = []

    def get_students(self):
        return self.__students.copy()

    def add_student(self, student):
        self.__students.append(student)

    def add_studants(self, *students):
        self.__students.extend(students)

    def display_studants(self):
        print(f"\nClass:-{self.grade}---Section:-{self.section}\n")
        for student in self.__students:
            print(f"\nName:- {student.name} -- Roll Number{student.roll_no}\n")

    def class_average(self):
        if not self.__students:
            return 0

        total = 0
        for student in self.__students:
            total += student.calculate_average_score()

        return total/len(self.__students)


class School:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.__classes = {}

    def add_class(self,classroom):
        key = (classroom.grade, classroom.section)
        self.__classes[key] = classroom

    def get_classes(self, grade, section):
        key = (grade, section)
        return self.__classes.get(key)

    def get_students_by_class(self, grade):
        print(f"class:- {grade}th students")
        found = False
        for(class_grade, section) ,classroom in self.__classes.items():
            if class_grade == grade:
                found = True
                print(f"Section:- {section}")

                for student in classroom.get_students():
                    print(f"Name:- {student.name}--Roll number:- {student.roll_no}")
        if not found:
            print("no students found")

    def display_class(self):
        print(f"\n list of class rooms are\n")
        for classes in self.__classes.keys():
            print(f'class:-{classes}\n')

    def display_all_students(self,classroom):
        print("All students from our school")
        all_students = classroom.get_students()
        for name,roll_no in all_students:
            print(f"Name:- {name}= {roll_no}")

lnps = School("LOHITHAKSHYA NATIONAL PUBLIC SCHOOL", "HUVINA HADAGALI")

class_8_a = Classroom(8, "A")
class_9_a = Classroom(9, "A")
class_10_a = Classroom(10, "A")

lnps.add_class(class_8_a)
lnps.add_class(class_9_a)
lnps.add_class(class_10_a)

s1 = Student(101,"Akash")
s2 = Student(102, "Anusha")

s3 = Student(201, "Sathish")
s4 = Student(202, "Sahana")

s5 = Student(301, "Sanjana")
s6 = Student(302, "Samruddhi") 

s1.add_marks(kannada = 95,english = 80, Hindi = 90, Maths = 85, Science = 90, Social = 80)
s2.add_marks(kannada = 85,english = 75, Hindi = 80, Maths = 70, Science = 75, Social = 80)
s3.add_marks(kannada = 75,english = 65, Hindi = 70, Maths = 60, Science = 65, Social = 70)
s4.add_marks(kannada = 65,english = 55, Hindi = 60, Maths = 50, Science = 55, Social = 60)
s5.add_marks(kannada = 55,english = 45, Hindi = 50, Maths = 40, Science = 45, Social = 50)
s6.add_marks(kannada = 96,english = 81, Hindi = 91, Maths = 86, Science = 91, Social = 81)
'''
class_8_a.add_studants(s1,s2)
class_9_a.add_studants(s3,s4)
class_10_a.add_studants(s5,s6)

lnps.get_students_by_class(8)
lnps.get_students_by_class(9)
lnps.get_students_by_class(10)

class_8_a.display_studants()
lnps.get_students_by_class(8)


#print(f"\nclass 8Th average:- {class_8_a.class_average():.2f}")


#print(f"\nclass 9Th average:- {class_9_a.class_average():.2f}")

print(f"\nclass 10Th average:- {class_10_a.class_average():.2f}")

students = [s1, s2, s3, s4, s5, s6]

lnps.display_class()'''
students = [s1, s2, s3, s4, s5, s6]

Rc = ReportCard()
#Rc.generate_all(students)
#print(s2.get_marks())
Rc.generate(s1)

# Learning how Git tracks changes