class person:
 def __init__(self,name,age):
      self.sname=name
      self.sage=age

 def printname(self):
         print(self.sname,self.sage)

class student:
   def __init__(self,sname,sage):
      person.__init__(self,name,age)

x= person("gsp",21)
x.printname()

#using super
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()

#passing some values
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    return f"{self.firstname} {self.lastname}"

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("gsp", "selva", 2019)
print(x.printname())
print(x.graduationyear)


#adding methods
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("nandhini", "selva", 2024)
x.welcome()
