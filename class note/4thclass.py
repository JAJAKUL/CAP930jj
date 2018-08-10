'''

print('spam eggs')
print('doesn\'t')
print("doesn't")
print('"yes," he said.')
print("\"yes,\" he said.")
print('"isn\'t," she said.')

print('I\'m in kolkata but I don\'t know that "you are also here".I\'ll see you in Howrah!. But I\'ii request \'you\' to bring "Rasogulla" for me')


print()

print(isinstance(4,object))
print(isinstance("hello",object))
print(isinstance(None,object))
print(isinstance([1,2,3],object))
#id(object) gives object's "identity".#
print(id(object))

"identity " is unique and fixed during an object's lifetime object are tagged with their type at run time
objects contain pointers to their data blob.
this means even small things take up a lot of space!


Variable are refrence to objects.





print((64).__sizeof__())

def compute(a,b,c):
    return (a+b)*c

obj=compute(1,2,3)
print(obj)
obj2=compute([1],[2,3],3)
print(obj2)
obj3=compute('l','olo',4)
print(obj3)


print()

print(1==1.0)
'''
print(1==1.0)
print(type(1)!=type(1.0))
gree="hello world!"
print(gree)
print(gree[4])
print('world' in gree)
print(len(gree))
#find the letter position#
print(gree.find('lo'))
#replace the value#
print(gree.replace('llo','y'))
#find the name and return true or false value#
print(gree.startswith('hell'))
print(gree.isalpha())

print()
print(gree.lower())
print(gree.title())
print(gree.upper())
print(gree.strip())
print(gree.strip('h'))
#convert the string into a list just use the split() function #
print('ham sath sath hai'.split())
print('10-08-2018'.split(sep='-'))
print('10/08/2018'.split(sep='/'))
print(','.join(['Eric','John']))


