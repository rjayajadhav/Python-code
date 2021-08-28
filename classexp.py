class  a:
    def __disp__(self):
        print("hello")
    def cal(self,a,b):
        c= a+b
        print(c)
class b(a):
    def show(self):
        print("hi friends")

a1=b()
a1.__disp__()
a1.cal(10,7)
a1.show()


