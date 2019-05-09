class Employee:
    empCount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary


    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)
    def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

employee = Employee("jgm",1000)
del  employee.name
setattr(employee,'name','金国民')
employee.displayCount()
employee.displayEmployee()
print("-------------------")
# 类的父类构成元素
print ("Employee.__doc__:", Employee.__doc__)
# 类名
print ("Employee.__name__:", Employee.__name__)
# 类定义的所在模块
print ("Employee.__module__:", Employee.__module__)
# 类的父类构成元素
print ("Employee.__bases__:", Employee.__bases__)
# 类的属性
print ("Employee.__dict__:", Employee.__dict__)
print("---------------------")

print(hasattr(employee,'age'))


print(hasattr(employee,'name'))
class Test:
    def prt(self):
        print(self)
        print(self.__class__)
t = Test()
t.prt()


class Job(Employee):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def myMethod(self):
        print("调用子类方法")

c = Job("JJJJ",10000)
c.myMethod()


class testInit:
    def __init__(self):
        print("无参构造")

    def __init__(self,name):
        print("无参构造")
