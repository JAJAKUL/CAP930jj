print(5 ** 2 )
print(7 / 2)
print(7 // 2)
print(2 * 3 == 5)
print(2 * 3) == 5
greeting = 'Hello'
print(greeting)
group = "wørld" # Unicode by default
print(group)

print(greeting + ' ' + group + '!') # => 'Hello wørld!'

s='jajakul'
print(s[0] ) # => I
print(s[1])  # => L
print(s[4])  # => E
print(s[6])  # => Y
#print(s[11]) #Error IndexError: string index out of range

#Negative Indexing starts from -1
print(s[-1]) #== N
print(s[-2]) #== O
print(s[-4]) #== T
print(s[-6])#==  P
print(s[::-1]) #==lukajaj
lis=[]
print(lis)
lis=[1,2,'jajakul']
print(lis)
lis.append(15)
print(lis)

Number = [1,2,3]  # List is decalred using squere brackets #Commas separate                     elements  
# Create a new list
print(Number)


# Lists can contain elements of different types
mixed_list = [10, 9, "Minutes"]
print(mixed_list)
#Append elements to the end of a list
mixed_list.append(10) # numbers == [10, 9, 'Minutes', 10]
print(mixed_list)

#Nested Lists
Nested_List= [Number,mixed_list]
print(Nested_List)

#Slicing Nested List
print(Nested_List[0])

print(Nested_List[0][1])

print(Nested_List[1][2:])
