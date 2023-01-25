d={'key1':'value1'}
d.update({'name':'user name'})
d.update({'branch':'Cse'})
d.update({'section':'A'})
print(d)
for i in d:
  print(i)



#Task
#create user input dictionary
l=[]
l1=['key1','key2']
for i in range(2):
  d={}
  for j in l1:
    a=input()
    d[j]=a
  l.append(d)
print(l)


#login system
#checking username and password
keys=['Name','Password']
l=[]
di={}
for i in range(2):
  di={}
  for j in keys:
    a=input()
    di[j]=a
  l.append(di)
print('Database:',l)
username=input('Enter username:')
password=input('Enter password:')
#method1
du={}
du['Name']=username
du['Password']=password
if du in l:
  print('You are successfully logged in')
else:
  print('Please enter correct credentials')



#method2
c=0
for i in l:
  if i['Name']==username and i['Password']==password:
    print('Credentials are correct')
    c=1
    break
if c==0:
  print('Please enter correct credentials')


#reading a 2d array
arr=[]
row_size=int(input('Enter row size:'))
col_size=int(input('Enter column size:'))
for i in range(row_size):
  col=[]
  for j in range(col_size):
    col.append(int(input()))
  arr.append(col)
print(arr)
#Accessing elements from the array


#sum of 2 2d-arrays
r1=int(input())
c1=int(input())
arr1,arr2=[],[]
for i in range(r1):
  col=list(map(int,input().split()))
  arr1.append(col)
for i in range(r1):
  col=list(map(int,input().split()))
  arr2.append(col)
print(arr1)
print(arr2)
#method1
for i in range(r1):
  for j in range(c1):
    print(arr1[i][j]+arr2[i][j],end=' ')
  print()




Slicing
list
list_name[start_index:stop_index:step_count]
string
string_name[start_index:stop_index:step_count]

#list_slicing
l=[1,2,3,4,5,6,7,8,9]
print('Without step size',l[0:5])
print('With step size',l[0::2])
print('Reverse the list:',l[::-1])


Negative indexing
Negative indexing starts with -1
Negative indexing starts from last of the list and string
[ ]
↳ 2 cells hidden
String
string.capitalize()
string.split()
string.join(list)
string.title()
string.lower()
string.upper()
string.islower()
string.isupper()
string.count(element)
string.isdigit()
string.isdecimal()
string.isalpha()
string.isalnum()
string.swapcase()
[ ]
#string methods
s='hello'
l=['h','e','l','l','o']
t='hello world'
lo='HELLO'
sc='HeLlo'
print('Capitalize:',s.capitalize())
print('Split:',s.split())
print('Join:',''.join(l))
print('Title:',t.title())
print('Lower:',lo.lower())
print('Upper:',s.upper())
print('Islower:',s.islower())
print('Isupper:',lo.isupper())
print('Count:',s.count('l'))
print('Swapcase:',sc.swapcase())
Capitalize: Hello
Split: ['hello']
Join: hello
Title: Hello World
Lower: hello
Upper: HELLO
Islower: True
Isupper: True
Count: 2
Swapcase: hElLO
String Formatting

#string formatting
first='Mr.X is'
age=39
last='years old'
#method 1
print(first,39,last)
#method2
print('Mr.X is {} years old'.format(age))
num=3.14
print('the square of {} if {:.6f}'.format(num,num*num))
print('the square of {:10} if {:.6f}'.format(num,num*num))
#method3
print(f"the square of {num} is {num*num:.5f}")#formatting strings(fstring)
print(f"the square of {num} is {num*num:10.5f}")
Mr.X is 39 years old
Mr.X is 39 years old
the square of 3.14 if 9.859600
the square of       3.14 if 9.859600
the square of 3.14 is 9.85960
the square of 3.14 is    9.85960




#calculator
num1=int(input('Enter num1:'))
num2=int(input('Enter num2:'))
s=input('Enter a symbol:')
op='+-/*%'
if s=='+':
  print(num1,s,num2,'=',num1+num2)
  exit(0)
if s=='-':
  print(num1,s,num2,'=',num1-num2)
  exit(0)
if s=='*':
  print(num1,s,num2,'=',num1*num2)
  exit(0)
while True:
  if s=='%':
    try:
      print(num1%num2)
      break
      exit(0)
    except ZeroDivisionError:
      print("Can't divide by zero")
      num2=int(input())
  elif s=='/':
    try:
      print(num1/num2)
      break
      exit(0)
    except ZeroDivisionError:
      print("Can't divide by zero")
      num2=int(input())
  else:
    break
if s not in op:
  print('Please enter valid operator')




  #read input from user and print the output without getting an error
try:
  a,b,c,d,e=map(int,input().split())
  print(a,b,c,d,e)
except:
  print('You enter invalid values')

Eval function
[ ]
↳ 1 cell hidden
Functions
Syntax
def function_name(arguments):
  statements

#addition of 2 numbers
def addition(num1,num2):
  return num1+num2
a,b=map(int,input().split())
print(addition(a,b))


#prime number
#method 1
def IsPrime(num):
  c=0
  if num<=0:
    return False
  for i in range(1,num+1):
    if num%i==0:
      c=c+1
    if c>2:
      return False
  return True
num=int(input())
print(IsPrime(num))


#method2
def IsPrime(num):
  c=0
  if num<=0:
    return False
  for i in range(2,num//2):
    if num%i==0:
      c=c+1
    if c>0:
      return False
  return True
num=int(input())
print(IsPrime(num))



Types of functions
with arguments,with return type
without arguments,with return type
with arguments,without return type
without arguments,without return type


#Regular function
def add(a,b):
  return a+b
a,b=map(int,input().split())
print(add(a,b))

#defalut value function
def add(n1,n2=0):
  print(n1+n2)
n1,n2=map(int,input().split())
add(n1)

#keyword arguments function
def printed(b,a,c,d):
  print('a:',a)
  print('b:',b)
  print('c:',c)
  print('d:',d)
printed(10,20,d=30,c=40)

#variable length function
import math as m
def add(c,d,e,*a):
  print(a)
  print(sum(a))
  print(m.prod(a))
add(1,2,3,4,5,6)

Recursion
-------
def check(n):
  print(n,end=' ')
  if n>0:
    check(n-1)
check(5)




