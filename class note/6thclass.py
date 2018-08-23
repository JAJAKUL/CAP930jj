emp=set()
emp=set([1,2,3,4,5])
bas = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
l=len(bas)

print(bas)
print(emp)
print(l)
p=emp.add(9)
print(p)
a=set("abracabra")
b=set("alacazam")
print(a)
print(b)
#set difference
print(a-b)
#union
print(a|b)
#intersection
print(a&b)
#Symmentric Difference
print(a^b)
