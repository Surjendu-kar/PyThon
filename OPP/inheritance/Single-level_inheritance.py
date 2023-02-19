class A:
    def feature1(self):
        print("Feature 1 Working")
    
    def feature2(self):
        print("Feature 2 Working")

class B(A): #inherite class A
    pass

b1 = B()
b1.feature1() 
b1.feature2()