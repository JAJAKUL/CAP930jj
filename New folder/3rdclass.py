'''
>>> len([])
0
>>> len("python")
6
>>> len([1,2,3,4,5,6,7])
7
>>> len([0,1,2,3,4,5,6,7])
8
>>> 'P' in "python'
SyntaxError: EOL while scanning string literal
>>> 'a' in 'jajakul'
True
>>> 25 in 14
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    25 in 14
TypeError: argument of type 'int' is not iterable
>>> 15 in [12,22,33,44,15]
True
>>> 11 in [22,33,44,55]
False

>>> 'jajakul' in ['a','b']
False
>>> 'jajakul' in ['jajakul','a']
True
>>> name=input("Enter your name placce")
Enter your name placcejajakul
>>> name
'jajakul'
>>> print("my name is ".name)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print("my name is ".name)
AttributeError: 'str' object has no attribute 'name'
>>> print("my name is "+name)
my name is jajakul
>>> print("my name is ",name)
my name is  jajakul



a=1
if a>0:
    print("Don't fall off!")#if statment are use 4 space#
b=10
if b<0:
    print("Don't fall off!")
else:
    print("Do fall on!")
if b<=4:
    print("Don't fall off!")
elif b==10:
    print("hgugu iugi")
else:
    print("Do fall on!")

n=int(input("enter the number"))
if n>10:
    print("bigher than 10: ",n)
elif b==10:
    print("equal")
else:
    print("lessthan 10: ",n)


word=input("enter the word: ")
reverse_word=word[::-1]
if word==reverse_word:
    print("palindrome")
else:
    print("not palindrome")

'''
print(bool(None))
print(bool(0.0))
print(bool([]))
print(range(1,5))
print(range(2,15,3))
for i in range(2,15,4):
    print(i)

for i in range(-2,-15,-4):
    print(i)
for i in range(10):
    if i==6:
        break
    print(i,end=',')

print()

for i in range(10):
    if i%2==0:
        print("Even",i)
        continue
        print("Odd",i)
print()

def prime(n):
    for i in range(2,n):
        if n%i ==0:
            return False
    return True
n=input("enter the number to be check prime: ")
for j in range(2,int(n)):
    if prime(j):
        print(j,"is prime")
    else:
        print(j," is not prime")
    
  
