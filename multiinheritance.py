class grandparent:
    def new1(self):
        print("i am grandfather")
class parent(grandparent):
    def new2(self):
        print("i am father")
class child(parent):
    a=10
obj=child()
obj.new1()
obj.new2()
