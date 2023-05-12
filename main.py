class Student :
    amount_of_students = 0
    def __init__(self,name,age, progress=0):
        self.name = name
        self.age = age
        self.progress = progress
    def greeting(self):
        print(f'Hello! My name is {self.name}, I am {self.age} years old.')
    def study(self):
        print(f'{self.name} is studying hard !!!')
        self.progress += 10
print('Amount of students',Student.amount_of_students)

student1 = Student(name = 'Pavlo',age = 14)
student1.greeting()
student2 = Student(name = 'Dmytro',age = 13)
student2.greeting()
print('Amount of students',Student.amount_of_students)
print('student1.progress',student1.progress)
print('student2.progress',student2.progress)
student1.study()
print('student1.progress',student1.progress)
print('student2.progress',student2.progress)
