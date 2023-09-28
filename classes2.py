# write a python program that creates a class called Person whoch contains name, 
# sex and professions as staes/attributes and working, study, and leave as its behaviours.
# demonstrate with examples the use of classes and objects.

class Person:
  def __init__(self, name, sex, profession):
    self.name = name
    self.sex = sex
    self.profession = profession

  def working(self):
    print(f'{self.name} is working as a {self.profession}')

  def study(self):
    print(f'{self.name} is studying to be a {self.profession}')

  def leave(self):
    print(f'{self.name} is leaving work')


person1 = Person('John', 'male', 'doctor')
person2 = Person('Mary', 'female', 'lawyer')
person3 = Person('Bob', 'male', 'teacher')


person1.working()
person2.study()
person3.leave()
        
