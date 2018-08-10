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
'''
"identity " is unique and fixed during an object's lifetime object are tagged with their type at run time
objects contain pointers to their data blob.
this means even small things take up a lot of space!


Variable are refrence to objects.



'''

print((64).__sizeof__())

def compute(a,b,c):
    return (a+b)*c

obj=compute(1,2,3)
print(obj)
obj2=compute([1],[2,3],3)
print(obj2)
obj3=compute('l','olo',4)
print(obj3)
