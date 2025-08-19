                         #FUNCTIONS
"""
def cal_avg(a , b , c):
    sum=a+b+c
    avg=sum/3            #function definition
    print(avg)

cal_avg(2,3,4) #function call

"""

#Question:01 find the length of list?
"""
heros=["iron man","thor","superman","flash"]
fruits=["orange","banana","apple"]

def length (list_parameter):
    print(len(list_parameter))

length(heros)
length(fruits)
"""





#Question:02 funtion to print elements in list in single line using forLoop?
"""
heros=["iron man","thor","superman","flash"]
fruits=["orange","banana","apple"]

def elemets (list):
    for values in list:
        print(values , end=" ")


elemets(heros)
print()
elemets(fruits)
"""








#Question:03 find factorial of n ?
"""
def factorial (n):
    fac=1
    for value in range(1 , n+1):
        fac*=value

    print(fac)

factorial(5)
"""






#Question:04 convert USD to PKR?
"""

def curreny_converter(usd):
    converter=usd * 300 
    print("Dollar",usd, "=","pakistani",converter)
    
curreny_converter(2)
"""







#Question:05 Even odd check function?


def checking(n):
    
    if( n % 2==0):
        print(n,"= Even")
    else:
        print(n,"= Odd")

number=int(input("Enter your number="))
checking(number)