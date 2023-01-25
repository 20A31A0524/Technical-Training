Inheritance
Single inheritance
Multi-level inheritance
Hierarchical inheritance
Multiple inheritance



#single inheritance
#parent class
class A:
  name=ani'
  age=26
#child class
class B(A):
  age=25
obj=B()
obj.name='Mahi'
print(obj.age)
print(obj.name)



#multi-level inheritance
class A:
  name='Teja'
  age=26
class B(A):
  age=10
class C(A):
  age=20
obj1=B()
obj2=C()
print(obj1.name)
print(obj2.name)
print(obj1.age)
print(obj2.age)


#example
#all best_friends are friends but all friends are not best_friends
#Moral --- all the parent class properties are accessible by child class but child class properties are not accessible by parent class
class Friend:
  f1,f2,f3='f1','f2','f3'
class Best_Friend(Friend):
  selected_frds=['meher','kusuma']
obj1=Best_Friend()
print(obj1.f1)
print(obj1.f2)
print(obj1.selected_frds)


#Hierarchical inheritance
class Person:
  name=''
  gender=''
  age=''
  pass
class Student(Person):
  s_name=''
  s_id=''
  s_branch=''
class Faculty(Person):
  salary=''
  subject=''



#example for Hierarchical 
class AI:
  b_name='AI'
class Machine_Learning(AI):
  m_name='Machine Learning'
class IOT(AI):
  i_name='Internet Of Things'
class Deep_Learning(AI):
  d_name='Deep Learning'
class NLP(AI):
  n_name='Natural Language Processing'
obj1=Machine_Learning()
obj2=IOT()
obj3=Deep_Learning()
obj4=NLP()
print('Parent:',obj1.b_name)
print(obj1.m_name)
print('Parent:',obj2.b_name)
print(obj2.i_name)
print('Parent:',obj3.b_name)
print(obj3.d_name)
print('Parent:',obj4.b_name)
print(obj4.n_name)




Multiple inheritance
#parent-1
class Pani_puri:
  def Sweet(self):
    print('Your sweet pani puri order is placed')
  def Hot(self):
    print('Your hot pani puri order is placed')
#parent-2
class Biryani:
  def Mandi(self):
    print('Your mandi order is placed')
class Customer(Pani_puri,Biryani):
  def Drive(self):
    print('Started to hotel')
pp=Customer()
pp.Drive()
pp.Sweet()
pp.Hot()
pp.Mandi()




#hybrid inheritance
#single+multiple
#single- Menus,Customer
#multiple- Panipuri,Biryani
class Pani_puri:
  def Sweet(self):
    print('Your sweet pani puri order is placed')
  def Hot(self):
    print('Your hot pani puri order is placed')
#parent-2
class Biryani:
  def Mandi(self):
    print('Your mandi order is placed')
class Menus(Pani_puri,Biryani):
  def menu(self):
    print('Please place your order!!')
class Customer(Menus):
  def Drive(self):
    print('Started to hotel')
pp=Customer()
pp.Drive()
pp.menu()
pp.Sweet()
pp.Hot()
pp.Mandi()




#rock,paper,scissor game
import random
l=['rock','paper','scissor']
c,h=0,0
while True:
  person=input('Human turn:')
  com=random.choice(l)
  print('Computer turn:',com)
  if person=='rock':
    if com=='paper':
      c=c+1
    elif com=='scissor':
      h=h+1
    else:
      pass
  elif person=='paper':
    if com=='scissor':
      h=h+1 
    elif com=='rock':
      c=c+1
    else:
      pass
  else:
    if com=='rock':
      c=c+1
    elif com=='paper':
      h=h+1
    else:
      pass
  print('Computer score:',c)
  print('Human score:',h)
  if h==5:
    print('Human wins')
    break
  if c==5:
    print('Computer wins')
    break




Human turn:paper
Computer turn: scissor
Computer score: 0
Human score: 1
Human turn:scissor
Computer turn: rock
Computer score: 1
Human score: 1
Human turn:rock
Computer turn: paper
Computer score: 2
Human score: 1
Human turn:paper
Computer turn: paper
Computer score: 2
Human score: 1
Human turn:rock
Computer turn: rock
Computer score: 2
Human score: 1
Human turn:paper
Computer turn: rock
Computer score: 3
Human score: 1
Human turn:paper
Computer turn: scissor
Computer score: 3
Human score: 2
Human turn:rock
Computer turn: paper
Computer score: 4
Human score: 2
Human turn:scissor
Computer turn: rock
Computer score: 5
Human score: 2
Computer wins



#Polymorphism
#method overriding is also known as runtime polymorphism
#same method name but diff signatures is overloading
#same method name and diff classes is overriding
class A:
  def method_1(self,a,b):
    print('Sum of 2 numbers:',a+b)
class B(A):
  def method_1(self,a,b):
    print('mul of 2 numbers:',a*b)
obj=B()
obj.method_1(10,20)



#n number- 101 - 010 - *(111-101)*
#method-1
n1=int(input())
n2=int(input())
a=bin(n1)
a=list(a[2:])
b=bin(n2)
b=list(b[2:])
for i in range(len(a)):
  if a[i]=='0':
    a[i]='1'
  else:
    a[i]='0'
for i in range(len(b)):
  if b[i]=='0':
    b[i]='1'
  else:
    b[i]='0'
a=''.join(a)
b=''.join(b)
n1=int(a,2)
n2=int(b,2)
print(n1^n2)


