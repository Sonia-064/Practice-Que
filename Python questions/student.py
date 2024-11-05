class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def display(self):
        print(f"Student: {self.name}, Grade: {self.grade}")


student1 = Student("John", "A")
student1.display() 
