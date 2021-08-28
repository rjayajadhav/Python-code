class animal:
    def disp(self):
        print("hello")
        a=int(input("enter the no:"))
        if a%2==0:
            print("Even")
        else:
            print("odd")
    def cal(self):
        x=int(input("enter the no:"))
        y=int(input("enter the value of y"))
        

class pet(animal):
    def show(self):
        print("welcommeee")

d=pet()
d.disp()
d.show()