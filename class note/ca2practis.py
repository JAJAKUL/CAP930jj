def func():
    print("hello world!")
func()
def func(name):
    print(name+" wolrd")
"""val=input("enter the string \n")
func(val)"""

def func3(country="india"):
    print("i am from "+country)

func3("US")
func3()
"""val1=input("enter the country name\n")
func3(val1)"""

def func4():
    return 111*111
print(func4())

def func4(a,b):
    return (111+a)*(111+b)
print(func4(2,3))
print(func4(0,0))


print("lambda function\n\n")
val=lambda a : a*4
print(val(2))

val1=lambda a,b,c : a*b/c

print(val1(4,2,5))
"""
Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous
function inside another function.
"""
def func5(n):
    return lambda a : a*n
lamval=func5(4)
print(lamval(5))

def func5(n):
    return lambda a : a*2
lamval=func5(3)
print(lamval(5))

print("\n\n")
print("while loop\n")
i=1
while i<5:
    print((10**i//9)*i)
    i+=1
for i in range(1,4):
    print((10**i//9)*i)

lis=["A","b","D"]
for i in lis:
    print(i)

for i in "jajakul":
    print(i)
st="jajakul"
for i in st:
    print(i)

ad=["jajakul"]
for i in ad:
    print(i)
for i in lis:
    print(i)
    if i=="b":
        break
for i in lis:
    if i=="b":
        break
    print(i)
for i in lis:
    if i=="b":
        continue
    print(i)

print("\n\n")
for i in "6":
    print(i)
for i in range(6):
    print(i) 
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


def A(n):
    val=n ** n
    def B(va7l):
        val2=va7l+va7l
        return val2
    val4=B(val)
    return val4

print(A(2))
print(A(3))





    





