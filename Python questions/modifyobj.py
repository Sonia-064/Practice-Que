class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Sonia", 20)

p1.age = 23
p1.myfunc()
print(p1.age)