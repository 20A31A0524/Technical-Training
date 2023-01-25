tuple
-------
tuple.index(element)
where element is persent in tuple
tuple.count(element)
counts the frequency of element in the tuple


t=(1,2,3,4)
print(type(t))
print(t.index(2))
print(t.count(1))


Set
s1.intersection(s2)
gives common elements in both sets
s1.union(s2)
gives all the elements from both the sets without duplicates
s1.difference(s2)
returns elements from the s1 which are not present in s2
s1.add(element)
adds element into the list
s1.difference_update(s2)


s1={1,2,3,4}
s2={2,5,6,1}
print('intersection:',s1.intersection(s2))
print(s1.union(s2))
print('difference:',s1.difference(s2))
s1.add(5)
print('after add:',s1)
s1.difference_update(s2)
print('difference update:',s1)



Conditional Statements
if(condtition):

 statements
elif(condition):

 statements
else:

 statements


 #even or odd
a=int(input())
print('Using if-else:')
if a%2==0:
  print(a,'is even')
else:
  print(a,'is odd')
print('Using ternary statement:')
print(a,'is even') if a%2==0 else print(a,'is odd')


Ternary Operator
print(statement) if condition else print(statement)


#printing week days
a=int(input('Enter the day number :'))
if a==1:
  print('Sunday')
elif a==2:
  print('Monday')
elif a==3:
  print('Tuesday')
elif a==4:
  print('Wednesday')
elif a==5:
  print('Thursday')
elif a==6:
  print('Friday')
elif a==7:
  print('Saturday')
else:
  print('Please enter valid number')


#>0 and <20 if even print weird  else normal
#20-30 print normal 
#>=30 and odd print normal else weird
num=int(input())
if num>0 and num<20:
  if num%2==0:
    print('Weird Number')
  else:
    print('Normal Number')
elif num>=20 and num<30:
  print('Normal Number')
else:
  if num%2==0:
    print('Weird Number')
  else:
    print('Normal Number')



Dictionary
It is key-value pair
key and value are seperated by colon(:)
Every pair is seperated by comma(,)
Dictionary Method

d.update({key:value})


d={1:'teja',2:'vani',3:'vasa'}
print(d)
dicti={
    'rollnum1':{'name':'abc','class':'1'},
    'rollnum2':{'name':'def','class':'2'}
}
print(dicti)


d={'s1':'A','s2':'B','s3':'C','s4':'D','s5':'E'}
d.update({'s1':'F'})
print(d['s1'])


Range function
range(start,end,step_size)


#range function
for i in range(1,10):
  print(i,end=' ')





List Comprehension
list=[x for x in range(start,end)]




#list comprehension vs normal method
l=[]
for i in range(10):
  l.append(i)
print(l)
#another way
l=[x for x in range(10)]
print(l)  



