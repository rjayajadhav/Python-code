class Employee:
    def __init__(self,fname,lname,dept,sal):
        self.firstname=fname
        self.lastname=lname
        self.department=dept
        self.salary=sal
    def disp(self):
        print(self.firstname,self.lastname,self.department,self.salary)
class test(Employee):

    x= Employee("jaya","jadhav","IT",20000)
    x.disp()