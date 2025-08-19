#Dictionary
"""
myInfo_dict={
"name":"huzaifa",
"age": 23 ,
"height": 5.10 ,
"favourate_subjects": {
    "Chemistry": "90%",
    "computer":"70%",
    "maths": "60%"
}
}

print(myInfo_dict.get("length"))
print(myInfo_dict)
"""
#Sets
"""
set={1,2,3,4,5 , "hello" , "hello",5}

print(type(set))
print("Duplicate values are removed",set)
print("the length of set is=",len(set),"Duplicate values are not count in length")
"""
"""
collection = set()
collection.add(10)
collection.add("hello")
collection.add("ali")
collection.add("world")
print(collection)
print(collection.pop(), "Gives random value")
"""

#Union & Intersection in sets
"""
set1={1,2,3,4}
set2={5,6,7,8,4}
print("Union of these sets are=",set1.union(set2))

print("intersection of these sets are=", set1.intersection(set2))
"""

#Question :01 store word meaning in python dictionary?
"""
dict={
    "table":["a piece of furniture" , "list of facts and figures"],
    "cat": "a small animal"
} 
print(dict)
"""
#Question:02 you are given a list of students.assume one class is req for 1sub how many classes are needed for all students?
#list give us repeating values so we use set
"""
list=["c++","python","jaava","python","javascript","java","python","java"
"c++","c"]
print(len(list),"wrong answer")

set={"c++","python","java","python","javascript","java","python","java"
"c++","c"}
print(len(set),"right answer")
"""
#Question:03 take subjects and marks from user and store in dictionary?
"""
marks ={}

x=int(input("enter phy marks="))
marks.update({"physics":x})

x=int(input("enter chemistry marks="))
marks.update({"chemistry":x})

x=int(input("enter math marks="))
marks.update({"math":x})

print(marks)
"""
#Question:04 store 9 and 9.0 in set and print both values use tuple in set?

set={9,9.0}
print("Its shows only one value=",set)

set={
    ("int",9),
    ("float",9.0)
}
print(set)