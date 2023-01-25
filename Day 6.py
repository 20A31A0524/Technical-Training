#language translator
from translate import Translator
translator= Translator(from_lang='english',to_lang="telugu")
translation = translator.translate("praneetha")
print(translation)


#method overriding
class A:
  def m1(self):
    print('in class A')
class B(A):
  def m1(self):
    print('in class B')
obj=B()
obj.m1()
obj.m1()


#method override
class Animal:
  def speaks(self):
    return "Animal can't speak"
class Dog(Animal):
  def speaks(self):
    return 'Dog barks'
class Cat(Animal):
  def speaks(self):
    return "Cat does't speak"
class Horse(Animal):
  def speaks(self):
    return "Horse can't speak"
d=Dog()
print('Dog class:',d.speaks())
c=Cat()
print('Cat class:',c.speaks())
h=Horse()
print('Horse class:',h.speaks())



Abstraction
to implement abstraction we make use of abc(Abstract Base Class) library



from abc import ABC,abstractmethod
class Area(ABC):
  @abstractmethod
  def calculate_area(self):
    pass
class Square(Area):
  def calculate_area(self):
    print('In Square area')
    pass
class Rectangle(Area):
  def calculate_area(self):
    print('In Rectangle area')
    pass
obj1=Square()
obj1.calculate_area()


Shift Operators

#right shift
print(2>>1)

#left shift
print(2<<1)



