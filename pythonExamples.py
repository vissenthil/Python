

numberLi = [1,2,3,4]
print(numberLi[3])
numberLi[3] = 19  # allow it is mutable
print(numberLi)
numtuple = (4,5,6)
print(numtuple[2])
#numtuple[2] = 5 # can not allow it is immutable
#numtuple[2] = 5

# Variables
a = True + False # True 1 Fale is 0
print(a)

a = {1, 2, 'a'}
#print(a[1])  #unorderd can not print
x = None
if x is None:
    print('No need to surprice i declare x No value')
name = 'senthilkumar'
a = list(name)
b = tuple(name)
c = set(name)
print(f'{a} as list')
print(f'{b} as Tuple')
print(f'{c} as set')

'''List Example Lists
The list type is probably the most commonly used collection type in Python. Despite its name, a list is more like an
array in other languages, mostly Javacript. In Python, a list is merely an ordered collection of valid Python values. A
list can be created by enclosing values, separated by commas, in square brackets:'''

int_list = [1,2,3,4,500]
str_list = ['senthil','Thalir','Aruthra','Krithihashini']
print(str_list)
# A list cab be Empty
empty_list = []
# The elements of a list are not restricted to a single data type, which makes sense given that Python is a dynamic
# language
mixed_list = [1,2,'Radha',455.56,6j] #6j is a complex number
print(mixed_list)
# A list can contain another list as its element:
list_with_another_list = [1,2,3,['senthil',3,4,67,44],(5,6,7),{3,5,6}]
print('A list can contain another list as its element:')
print(list_with_another_list)
list_index = '''The elements of a list can be accessed via an index, or numeric representation of their position. Lists in Python are
zero-indexed meaning that the first element in the list is at index 0, the second element is at index 1 and so on:'''
print(list_index)
print(list_with_another_list[3][0])
List_indices = '''Indices can also be negative which means counting from the end of the list (-1 being the index of the last element).
So, using the list from the above example:'''
names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
print(names[0]) # Alice
print(names[2]) # Craig
print(List_indices)
print(names[-1])
print('Lists are mutable, so you can change the values in a list:')
names[0]= 'Thalir'
print(names)
print('Besides, it is possible to add and/or remove elements from a list:')
names.append('SenthilKumar')
print(names)
print('Add a new element to list at a specific index. L.insert(index, object)')
names.insert(1,'Aruthra')
print(names)
print('Remove the first occurrence of a value with L.remove(value), returns None')
names.remove('SenthilKumar')
print(names)
print('Get the index in the list of the first item whose value is x. It will show an error if there is no such item.')
print(names.index('Aruthra'))
print('Count length of list')
print(len(names))
print('count occurrence of any item in list')
a = [1,1,2,3,1,3,5,6,7,9]
b = int(input('Please enter value to check count:'))
print(a.count(b))
print('Reverse the list')
a.reverse()
print(a)
print('Remove and return item at index (defaults to the last item) with L.pop([index]), returns the item')
a.pop()
print(a)
a.pop(4) # by using index
print(a)
print('You can iterate over the list elements like below:')
for values in a:4
    print(values)