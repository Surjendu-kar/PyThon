class Student:
    def __init__(self,name,roll) -> None:
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()

    def show(self):
        print(self.name,self.roll)
        self.lap.show()
    class Laptop:
        def __init__(self) -> None:
            self.brand = "HP"
            self.cpu = "i7"
            self.ram = 8

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = Student("surjo",105)
s2 = Student("Rahul",501)

s1.show()
s2.show()
print(s1.lap.brand,s1.lap.cpu)

# lap1 = s1.lap 
lap1 = Student.Laptop()
lap2 = s2.lap
