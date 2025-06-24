class myClass:
  x=5
y=myClass()
print(y.x)

class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age

#using str() function
p1 = Person("gsp",20)
print(p1.name,p1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

#Use the words mysillyobject and abc instead of self:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()