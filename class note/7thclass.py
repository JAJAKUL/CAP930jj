def que():
    """this function without parameter"""
    val=3**3
    print(val)

que()
def que(a):
    """this function with parameter"""
    val=a**3
    print(val)

que(4)

def add(val1,val2):
    """This function add two number with parameter and return value"""
    new_val=val1+val2
    return new_val
obj=add(10,30)
print(obj)


def addtuple(val,val2):
    obj=val+val2
    obj2=val * val2
    tub=(obj,obj2)
    return tub
print(addtuple(3,6))



new_val=10
def add(val):
    global new_val
    new_val=new_val **val
    return new_val
print(add(2))
new_val=20
print(add(2))

new_val=10
def add(val):
    global new_val
    new_val=new_val **val
    return new_val
print(add(2))
print(new_val)


print()

def A(n):
    val=n ** n
    def B(val):
        val2=val+val
        return val2
    val4=B(val)
    return val4

print(A(2))
print(A(3))
def power(val,pow=1):
    return val ** pow
print(power(4,2))
print(power(4))


print("\n\n\n\n")
n=int(input("enter the 1st number\n"))
m=int(input("enter the 1st number\n"))
p=int(input("enter the option"))

while(p):
    case
def add(n,m):
    return print(n+m)
def mul(n,m):
    return print(n*m)
def div(n,m):
    return print(n/m)
add(n,m)
mul(n,m)
div(n,m)






