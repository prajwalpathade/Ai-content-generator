class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("your name is:",self.name,"and your marks is:",self.marks)


    def avg_marks(self):
        a=0
        for i in self.marks:
            a+=i
        print("Your avg marks is:",a/3)


s1=Student("Prajwal",[98,32,55])
s1.avg_marks()

s1.name="Tony Stark"
s1.avg_marks()

