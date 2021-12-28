

print('For loop Examples')
tup = [(1,2,3),(4,5,6),(6,7,5),(4,2,4)]
print(tup)
print( 'Looping through Tuples:-')
for item in tup:
    print(item)
print('tuple unbacking------------')
for (a,b,c) in tup:
    print(a,b,c)
print('To pring Each element in a tuple')
for (a,b,c) in tup:
    print(a)
    print(b)
    print(c)
print('Looping through Distionary ')
mydictionary = {'k1': 1, 'k2': 2, 'k3': 3}
for item in mydictionary:
    print(item)

print( 'To get Key and values')
for item in mydictionary.items():
    print(item)
print( 'Only to get Keys')
for item in mydictionary.keys():
    print(item)
print( 'Only to get values')
for item in mydictionary.values():
    print(item)
print( 'Dictionary Unbacking')
for key,values in mydictionary:
    print(key + ',' + values)
else:
    print('Else statement in for loop')
print('Loop using Range operator')
for item in range(10):
    print(item)
print('Loop through String')
for letter in 'Hello Senthil Kumar':
    print(letter)
list_index = 0
print('Loop through each index in a string')
for letter in 'Hello Senthil Kumar':
    print('Letter at index {} is {}'.format(list_index,letter))
    list_index +=1
print('Another way of loop through each in of a string')
word = 'Hello Senthil Kumar'
list_index = 0
for letter in word:
    print(word[list_index])
    list_index +=1

print('Using enumerate operator to automatically index')
for item in enumerate(word):
    print(item)
for index,item in enumerate(word):
    print(index,item)
print('Zip operator in Python')
mylist = [1,2,3,4]
mylist1 = ['Senthil','Thalir','Aruthra','Kruthihashini']
mylist3 = [100,200,300,400]
print(zip(mylist,mylist3,mylist1))
for item in zip(mylist,mylist1,mylist3):
    print(item)
print('Unbacking zip operator ')
for a,b,c in zip(mylist,mylist1,mylist3):
    print(b)
print(tuple(range(10)))

print(list(range(10)))
