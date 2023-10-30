
# design a class with private attributes and public methods and try to manipulate them.
class Person:
    def __init__(self,name,age):
        self.name=name
        self._age=age #private attribute

    def get_name(self):
        return self.name
    
    def set_name(self,new_name):
        self.name=new_name

    def get_age(self):
        return self._age
    
    def set_age(self,new_age):
        if new_age>0:
            self.age=new_age
        else:
            print("Age cannot be zero or negative.")

person=Person("Nina",22)
print("Original Name: ",person.get_name(),"\nOriginal Age: ",person.get_age())

person.set_name("Diana")
person.set_age(40)
print("Updated name: ",person.get_name(),"\nNew Age:", person.get_age())

# since age is private, it will remain unchanged.







