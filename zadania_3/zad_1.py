class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def isPassed(self):
        average = sum(self.marks) / len(self.marks)
        return average > 50


student1 = Student("Jan", [60, 70, 80])
student2 = Student("Anna", [30, 50, 60])

print(f"{student1.name}: {student1.isPassed()}")
print(f"{student2.name}: {student2.isPassed()}")
