#Question:01 calculate avg of three subjects?
"""
class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

                     #METHOD

    def cal_avg(self):
        sum=0
        for val in self.marks:
            sum+=val

        print(self.name , "has an average marks=", sum/3)

            #OBJECT

s1=Student("Huzaifa", [98,99,68])
s1.cal_avg()
"""


#Question 2 create acount take atttributes balence and account no also create credit and debit methods?


class Account :
    def __init__(self , bal ,account):
        self.bal=bal
        self.account=account
    
    #debit Method

    def debit(self , amount):
        self.bal-=amount
        print("the amount of ",amount,"is debited")
        print("current balence is=",self.bal)

    #Credit Method


    def credit(self , amount):
        self.bal+=amount
        print("the amount of ",amount,"is credited")
        print("your current balence is=",self.bal)



a1=Account(500,1234555)
print(a1.bal , a1.account)
a1.debit(200)
a1.credit(500)

a2=Account(700 ,5794673)
print(a2.bal,a2.account)
a2.credit(100)