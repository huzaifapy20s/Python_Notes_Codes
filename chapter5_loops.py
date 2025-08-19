                    #LOOPS
#while loop
"""
count =1
while count <=5 :
    print("Hello world")
    count +=1
"""


"""
increment of 1
i=1
while i<=5:
    print(i)
    i+=1
"""


"""
decrement by 1
j=5
while j>=1:
    print(j)
    j-=1
"""


#Question 1: print no from 1 to 100 & 100 to 1 using while loop?
"""
i=1
while i<=100:
    print(i)
    i+=1
print("1 to 100 loop ended")
j=100
while j>=1:
    print(j)
    j-=1
"""


#Question 2 take input from user and print table of that number?
"""
no=int(input("ENTER NUMBER="))

count =1
while count<=10:
    print(no,"*",count,"=",count*no)
    count+=1
"""

#Question:03 print list [1 4 16 25 36 ...100] by using while loop?
                    #Traversing
"""                  
list =[1, 4, 16, 25 ,36 ,49 ,64, 81 ,100]
index=0
while index<len(list):
    print(list[index])
    index+=1
print (index)
"""


#Question:04 Searching in tuple(1, 4, 16, 25 ,36 ,49 ,64, 81 ,100)use break
"""
tuple=(1, 4, 16, 25 ,36 ,49 ,64, 81 ,100)
number =25
index=0
while index<len(tuple):
    if (tuple[index]==number):
        print("number found at =",index)
        break
    else:print("number not found")
    index+=1
"""

#Question:05 find the sum of natural numbers like 5?
"""
no=2
index=1
sum=0
while index<=no:
    sum+=index
    index+=1
print(sum)
"""

#continue example:
"""
i=1
while i<=10:
    if(i %2 ==0 ):
        i+=1
        continue #skip
    print(i)
    i+=1
"""

                      
                      #For Loops
"""
list =[1 ,2 ,3 ,4 ,5]

for val in list :
    print(val)
"""
"""
tuple=("apple","mango","banana")
for fruitNames in tuple:
    print(fruitNames)
"""

#Question:01 [1, 4, 16, 25 ,36 ,49 ,64, 81 ,100] print this using loop?


"""
list=[1, 4, 16, 25 ,36 ,49 ,64, 81 ,100]
num=64
index=0
for val in list:
    index+=1
    if(val==num):
        print(index,"num is found=",val)
        break
    else :
        print(index,"num not found")
"""    



#Question:02 search a number in tuple (1, 4, 16, 25 ,36 ,49 ,64, 81 ,100) ?
"""
tuple=(1, 4, 16, 25 ,36 ,49 ,64, 81 ,100)
no=int(input("Enter a number for search"))

for value in tuple:
    if(no==value):
        print("Number is found=",value)
        break
    else:
        print("no not found")
"""
#Question:03 find the factorial of first n natural no?
"""
no=5
factorial=1 #always take 1 in factorial
for val in range(1 , no+1 ):
 factorial *=val
 print(factorial)
"""
 
                    #RANGE in for loop

"""
for val in range(5):
    print(val)

for val in range(2,100,2): #even numbers
    print(val)

for val in range(1,100,2): #odd numbers
    print(val)
"""


#Question:01 print no from 1-100 & 100 -1 using range?
"""
for val in range(1,101):
    print  (val)

for val in range(100,0,-1):
    print(val)
"""

#Question:02 print the table of no n?
"""
no=int(input("enter a number="))

for table in range(1 , 11 ):
    
    print(no*table)
"""