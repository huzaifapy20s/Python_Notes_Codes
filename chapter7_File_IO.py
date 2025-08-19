"""
f= open("demo.txt","r")
data=f.read()
print(data) 
f.close()
"""


#Question:01 create a file and add data in it?Replace java with python?
"""
with open("practice.txt","r") as f:
    data=f.read()
    newdata=data.replace("java","python")
    print(newdata)

#replace data in main file

with open("practice.txt","w") as f:
    data=f.write(newdata)
"""


# Question:02 searching word learing in file?


with open ("practice.txt","r") as f:
    data=f.read()
    if(data.find("learning")!=-1):
        print("found")
    else:
        print("not found")







  
  
   
