class Student(object):
    def __init__(self,fname,lname,age):
        self._fname=fname
        self.lname=lname
        self.age=age

    def get_name(self):
        return self._fname
    
def main():
    student=Student('Diana','clarissa')
    tst=student.fname
    print(tst)

student=Student('Diana','clarissa',12)
print(student)

