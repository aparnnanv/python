class parent():
    def greet(self):
        print("phyton programming")
class child1(parent):
    a=30
class child2(parent):
    b=45
class child3(parent):
    c=70
obj1=child1()
obj2=child2()
obj3=child3()
print(obj1.a)
obj1.greet()
obj2.greet()
obj3.greet()
