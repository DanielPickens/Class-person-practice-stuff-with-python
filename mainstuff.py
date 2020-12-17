class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __getitem__(self,key):
        print ("Inside `__getitem__` method!")
        return getattr(self,key)

p = Person("Daniel",31)
print (p["age"])
