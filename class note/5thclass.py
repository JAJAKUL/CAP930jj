roll_no=[]
for i in range(1,31):
    roll_no.append(i)

print(roll_no)

roll=[2,1,4,3,5,6,3,8,7,4]
print(roll.sort())
#finit, oredered, mutable, sequence of elements #
# list #
easy=[1,2,3]
print(easy)
# dictionary#
empty={}
print(type(empty))
print(empty==dict())
a=dict(one=1,two=2,three=3)
print(a)
b={"one":1,"two":2,"three":3}
print(b)
print(a==b)

print()
bio=dict(FName='jajakul',LName='islam',Email='jajakulislam@gmail.com',phone=8436748148, Regno=11707260)

print(bio)
#print(bio['mname'])  key error#
print(bio['FName'])
bio['Email']='ijajakul@gmail.com'
print(bio)
#dictionary using list#

data={'number':[1,2,3,4,5],'math':[11,33,44,55,66]}
print(data)
print(data.get('math'))
print(data['math'])
print(data.get('mathd'))
obj=data.get('english',[])
print(len(obj))
#data.pop('Email')#
print(data.keys())
print(data.values())
print(data.items())
print(len(data.keys()))
('FName','jajakul') in data.items()
for value in data.values():
    print(value)

print(len(data))
value in data.values()
obj1=data.copy()
print(obj1)
# tuple
tap=("name","reg","email")
print(tap)
print(tap[2])
print(tap[:2])
p="reg" in tap
print(p)
t=12345,54321,'hello'
print(t)
print(type(t))
x,y,z=t
print(x)
print(z)
print(y)

x=4
y=2

x=x+y
y=x-y
x=x-y
print(x)
print(y)
x,y=y,x
print(x)
print(y)


