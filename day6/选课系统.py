#!_*_coding:utf-8_*_
class School(object):
    def __init__(self,name,addr,city):
        self.name = name
        self.addr = addr
        self.city = city

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex =sex

class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade,course):
        super(Student,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade
        self.course = course

    def pay_tuition(self, amount):
        print("%s has paid tution for $%s" % (self.name, amount))

class Teacher(SchoolMember):
    def __init__(self, name, age, sex, course):
        super(Teacher,self).__init__(name,age,sex)
        self.course = course

class Course(object):
    def __init__(self,name,school,price):
        self.name = name
        self.school = school
        self.price = price