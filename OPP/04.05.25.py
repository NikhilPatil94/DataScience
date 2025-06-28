class A:
    def add(self, a, b):
        print(f"hello : a value is {a} & b value is {b}")
    
    def add(self, a, b, c):
        print(f"hello : a value is {a} & b value is {b} & c is {c}, Final")

object = A()

object.add(1,2)