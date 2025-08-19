
#Question:1 take input users first name and find lenght of it?

"""
firstName =input("Enter Your First Name :")
print(firstName)
print("LENGTH OF YOUR NAME IS:",len(firstName))
"""
#Question:2 find the occurance of dollar sign in the string?
"""
string = "I love $ and $ is my favorite character"
print(string)
print("NO OF $ WHICH OCCUR IN THIS STRING ARE",string.count("$"))
"""

#Question:3 if elseif else statements
""""
marks = int(input("Enter marks"))
if(marks >=90):
    print("your grade is A")
elif(marks <90 and marks >=80):
    print("your grade is B")
elif(marks <80 and marks >=70):
    print("your grade is C")
elif(marks <70 and marks >=60):
    print("your grade is D")
else:
    print("you are FAIL") 

print(type(marks))
"""
#NESTING 
"""""
age =50
if(age>=60):
    if(age>=40):
        print("cannot drive")
    else:print("can drive")

else: print("Cannot drive")
"""
# Question :04 Check Even and odd
"""
number =int(input("Enter Number to Check Even OR Odd="))
if(number % 2 ==0 ):
    print("THIS NUMBER IS EVEN")
else:
    print("THIS NUMBER IS ODD") 
"""

#Question :05 check the gretest of 3 numbers entered by user
"""
a = int(input("first no="))
b = int(input("second no="))
c = int(input("third no="))

if (a>b and a>c):
    print("A is greatest")
elif(b>a and b>c):
    print("B is greatest")
else:
    print("C is greatest")
"""
 # Question :06 check if number is multiple of 7 or not

number = int(input("Enter number="))

if  (number % 7 ==0):
    print("YES This number is multiple of 7")

else:
    print("NO this number is not a multiple of 7")