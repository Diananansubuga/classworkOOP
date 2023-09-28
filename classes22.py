class Person:
  def __init__(self, name, sex, profession):
    self.name = name
    self.sex = sex
    self.profession = profession
    self.status = "working"  # Default status is "working"

  def working(self):
    if self.status == "working":
      print(f'{self.name} is working as a {self.profession}')
    else:
      print(f'{self.name} is not working')

  def study(self):
    if self.status == "studying":
      print(f'{self.name} is studying to be a {self.profession}')
    else:
      print(f'{self.name} is not studying')

  def leave(self):
    if self.status == "leave":
      print(f'{self.name} is on leave')
    else:
      print(f'{self.name} is not on leave')


person1 = Person('Toby', 'male', 'doctor')
person2 = Person('Tirzah', 'female', 'lawyer')
person3 = Person('Alala', 'male', 'teacher')


person1.working()
person2.study()
person3.leave()













person1.status = "studying"
person2.status = "leave"
person3.status = "working"

person1.working()
person2.study()
person3.leave()