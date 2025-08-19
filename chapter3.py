#list in python
"""
marks=[20.0,30.1,40.2,60,80,100]
print( "whole list:",marks)
print ("marks at zero index=",marks[0])
print ("marks at 2 index=",marks[2])
print ("marks at 4 index=",marks[4])
print("length of marks list is=",len(marks))
"""
#methods in list:
"""
marks=[20.0,30.1,40.2,60,80,100]

marks.append(20.2)
print(marks)

marks.sort()
print(marks)

marks.sort(reverse=True)
print(marks)

marks.reverse()
print(marks)

marks.insert(3,50.5)
print(marks)

marks.remove(50.5)
print(marks)

marks.pop(0)
print(marks)
"""

#Question:01 input from user there 3 favt fruits and store them in list
"""
fruit1=input("ENTER FIRST FRUIT =")
fruit2=input("ENTER SECOND FRUIT =")
fruit3=input("ENTER THIRD FRUIT =")

Fruit_list=[fruit1,fruit2,fruit3]
print("YOUR FRUIT LIST IS:",Fruit_list)
"""
#Question:02 check the list is paladrome or not
"""
list1=[1,2,1]
list2=list1.copy()
list2.reverse()
if(list2==list1):
    print("paladrome")
else:
    print("Not paladrome")
 """
                       #TUPLES
#Question:03 count the number of students with A grade in tuple (c,d,a,a,b,d,a)?
"""
grade=("B","A","C","A","A")
print (grade.count("A"))
 """
#Question:04 sort the values from A TO D in list

grade=["B","A","C","A","A","D","C"]

grade.sort()
print("SORTED LIST IS:",grade)