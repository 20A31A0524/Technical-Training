Data types
--------------
integer
float
string
single quote
double quote
triple quote
doc string- which is multi line string and used for documentation
boolean
True
False
complex
used for finding roots
list - []
mutable
elements in list are objects
a list is a collection of variables which are of diff types
tuple - ()
immutable
collection of elements
set - {}
mutable
duplicates are not allowed
Collection of unique variables of diff types
doesnot follow insertion order i.e, unordered


#difference between single elemment and more tham one element in tuple
a=(1,2,3)
print(type(a))
b=(1)
print(type(b))


#set
s={'a','b','c','c','a'}
print(s)



Naming conventions
using underscore - name_is
using camel case - NameIs
Operators
Arithematic operator
+,-,*,/,%,//
Comparison operator
<,>,<=,>=,==,!=
Assignment operators
=,+=,-=,*=,/=,%-
Logical operator
and , or, not
Membership Operators
in,not in
Bitwise Operator
&,|,^
Identity Operator
is, not is
Ternary Operator
(condition) ? True_Part : False_Part
3 operands
[ ]
#and operator usage
a=23
b=7
print(a and b)
print(bin(a and b))
c="0b0101"
print(type(c))
7
0b111
<class 'str'>
[ ]
#program
a,b=2,3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a<b)
print(a>b,a>=b,a<=b,a!=b)
print(a and b)
print(a or b)
print(not a)
5
-1
6
0.6666666666666666
0
2
True
False False True True
3
2
False
LIST
list.append(element)
list.pop(index)
index is not mandatory
returns popped element
list.remove(element)
element is mandatory
returns None
list.insert(index,element)
at a certain index the element is added
return None
list1.extend(list2)
list2 elements extended to list1
list.count(element)
counts the frequency of element in the list
len(list)
returns the length of list
list2=list1.copy()
copies list1 elements into list2
list.reverse()
reverse the list
list.sort(reverse=True/False)
sorts the list in ascending order
reverse is optional
perform operation on same list
list2=sorted(list,reverse=True/False)
sort the list
perform the operations using the list elements and stores in another list
reverse is optional
list.clear()
clears the list elements
[ ]
#list
l=[]
l1=[10,20]
l.append(1)
l.append([1,2,3])
l.append('hello')
l.append(5.26)
print('after using append',l)
l.insert(1,'hai')
print('after using insert',l)
l1.extend(l)
print('after extended',l1)
l2=l1.copy()
print('after copying',l2)
after using append [1, [1, 2, 3], 'hello', 5.26]
after using insert [1, 'hai', [1, 2, 3], 'hello', 5.26]
after extended [10, 20, 1, 'hai', [1, 2, 3], 'hello', 5.26]
after copying [10, 20, 1, 'hai', [1, 2, 3], 'hello', 5.26]
Type Casting
The string characters must be numbers for converting the type of string into int and float

string-int
int(string)
string-float
float(string)
int-string
str(integer)
string-list
list(string)
list type conversion
str-int
list(map(int,list))
str-float
list(map(float,list))
int-str
list(map(str,list))
[ ]
a=['0','1']
l=list(map(int,a))
print(l)
[0, 1]
Reading inputs
reading string
input()
reading integer
int(input())
reading float
float(input())
[ ]
#programming session
#calculator
a=int(input('Enter a:'))
b=int(input('Enter b:'))
c=input()
if c=='+':
  print(a,'+',b,'=',a+b)
elif c=='-':
  print(a,'-',b,'=',a-b)
elif c=='*':
  print(a,'*',b,'=',a*b)
elif c=='/':
  if b==0:
    print("Can't do division")
  else:
    print(a,'/',b,'=',a/b)
elif c=="//":
  print(a,'//',b,'=',a//b)
else:
  print(a,'%',b,'=',a%b)
Enter a:55
Enter b:8
+
55 + 8 = 63
[ ]
#printing username and password
username=input()
passw=input()
if len(passw)<8:
  print('Please enter atleast 8 character length password')
else:
  print('Username:',username)
  print('Password:',passw)
Praneetha
123456789
Username: Praneetha
Password: 123456789
[ ]
#square of numbers
n=int(input('Enter the number:'))
s=str(n)
l=list(s)
l=list(map(int,l))
for i in l:
  print(i*i)

Enter the number:12345
1
4
9
16
25
[ ]

