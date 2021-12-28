
l = [1,2,3,4,4,'senthilkumar','Thalir','Aruthra','Krithihashini']
print(len(l))
print('Thalir' in l)
print('894' in l)
# append method will append a value end of the list
l.append('my New son will come')
print(l)
l.insert(5,'Chennai')
print(l)
l.insert(45,'Mudachikkau') # if idex is not available in the list it will insert at the lost position
print(l)
l.remove('Chennai') # remove the give  element from the list
print(l)
l.reverse() # reverse the list:
print(l)
l2 = [1,2,3,4,6]
l3 = [45,67,85,56]
print('list L2:',l2)
print('List L3:', l3)
print('Extend method of list extend will unwrap the list and include into another list')
l2.extend(l3)
print(l2)
l.extend('ramue')
print(l)
l.pop() # removes the values at the end
print(l)
l.pop(6) # remove the value from given idex
print(l)
# pop will remove elsement based on index and Remove will remove the element based on values took in parameter
# if more then one element it will remove only at the very very first potion.
print('Remove element from the list listname.remove(value)')
l.remove(4)
print(l)
l.clear() # clear all the list
print('Data cleared')
print(l)
l1 = [1,2,3,4,4,'senthilkumar','Thalir','Aruthra','Krithihashini',['apple','bana','Orange']]
l1.reverse() #will reverse the element in a list
print(l1)
l1[0].reverse()# will reverse list of list at index 0
print(l1)
print('Split Method in List ')
string1 = 'This is a sample text i am going to use split methods of  list'
string1.split() # split the each word in a given string
print(string1.split())
for i in string1.split(): # to split each word one by one
    print(i)
print('List comprehension Operation')
l4 = [1,2,3,4,5]
sqrofList = [i**2 for i in l4]
print(sqrofList)
name = 'Senthil Kumar'
print([i for i in name])
l5 = [1,2,3,4,5,6,7,8,9,10]
a= [i for i in l5 if i%2==0] #odd numbers
b = [i for i in l5 if i%2!=0] #even numbers
print(a)
print(b)
d = ([j for j in l5 if j%2!=0], [i for i in l5 if i%2==0])
print('d is now :',d)
#c = [i+j for i in a for j in b]
c = [a[i]+b[i] for i in range(len(a))] # adding two list by each index
print(c)
additonOfList = []

for i in range(len(a)):
    additonOfList.append(a[i]+b[i])

print(f'Added List{additonOfList}')
thislist = ["apple", "banana", "cherry"]
for i in thislist:
    print(i)
newlist = [ x for x in thislist if 'a' in x ]
print(newlist)
thislist = ["apple", "banana", "cherry"]
newlist = [ x.upper() for x in thislist ]
print(newlist)
newlist = ['hello ' + x for x in thislist]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != 'banana' else 'Orange' for x in fruits]
# Here it check the fruits if not equal to banana print that fruit if banana then print it as Orange instead of banana
print(newlist)
fruits1 = ["apple", "mango","banana", "cherry", "kiwi", ]
fruits1.sort()
print('Sorted List by default ascending order',fruits1)
fruits1.sort(reverse=True) # To sort the list Descending order.
print('Sorted List by Descending order is :', fruits1)

''' You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first):'''
''' Sort the list based on how close the number is to 50:'''
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort() # sort is sensitive by default it will sort capital letters first and then small letter.
print(thislist)
# To make it insensitive
thislist.sort(key=str.lower)
print('Sorted using insensitive method:',thislist)