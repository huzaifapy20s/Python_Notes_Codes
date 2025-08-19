
class order:
    def __init__(self, item,price):
        self.item=item
        self.price=price

    def __gt__(self,o2 ):  #it takes only two values thats why use self& other value
       return self.price > o2.price


o1=order("mango","200")
o2=order("banana","600")
print(o1 > o2)

        