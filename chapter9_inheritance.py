
#SINGLE INHERITANCE 
"""
class parent:
    @staticmethod
    def start():
        print("car is started")

    @staticmethod
    def stop():
        print("car is stoped")

#single inheritance
class child(parent):
    def __init__(self ,name ,model):
        self.name=name
        self.model=model

c1=child("mehran","2007")
print(c1.name , c1.model)
c1.start()

c2=child("swift","2018")
print(c2.name,c2.model)
c2.stop()
"""


#MULTI LEVEL INHERITANCE:
"""
class Grandparent:
    @staticmethod
    def start():
        print("car is started")

    @staticmethod
    def stop():
        print("car is stoped")

#single inheritance
class parent(Grandparent):
    def __init__(self ,name ,model):
        self.name=name
        self.model=model
# multi inheritance child has properties of both parent and grandparent
class child(parent):
    def __init__(self ,color ,speed):
        self.color=color
        self.speed=speed

c1=child("red","100")
print(c1.color , c1.speed)
c1=parent("mehrn","2007")
print(c1.name,c1.model)
c1.start()
"""


"""
class Grandparent:
    @staticmethod
    def start():
        print("car is started")

    @staticmethod
    def stop():
        print("car is stoped")

#single inheritance
class parent:
    def __init__(self ,name ,model):
        self.name=name
        self.model=model
    @staticmethod
    def method_race():
        print("racing car")

# multiple inheritance child has properties of both parent and grandparent
class child(Grandparent,parent):
    def __init__(self, name,model,color ,speed):
        parent.__init__(self,name,model) #call parent constructor
        self.color=color
        self.speed=speed

c1=child("mehran","2007","red","150km/h")
print(c1.name,c1.model,c1.color,c1.speed)
c1.start()
c1.method_race()
"""



#practice question
"""
class circle:
    def __init__(self , radius):
        self.radius = radius

    def area(self):
        area= 3.14 * self.radius **2
        print("area of circle=",area)
    
    def parameter(self):
        pmtr= 2 * 3.14 * self.radius
        print("perimeter of circle=",pmtr)

        
a1=circle(21)
a1.area()
a1.parameter()
"""



#Question:02




class employee:
    def __init__(self ,role , department ,salary):
        self.role=role
        self.department=department
        self.salary=salary
   
    def showDetails(self):
        print("Employee Role=",self.role)
        print("Employee Departent=",self.department)
        print("Employee Salary=",self.salary)


class engineer(employee):
    def __init__(self,name,age, role, department, salary):
        super().__init__(role, department, salary)
        self.name=name
        self.age=age

emp1=engineer("ali","22","head","computer","20k")
print(emp1.name ,emp1.age)
emp1.showDetails()




    