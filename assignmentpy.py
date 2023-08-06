
#find if any given string is palidrome or not
print('Find if any given string is palidrome or not?')
get_input = input('Please enter a string to find palindrome or not:')

ln = len(get_input) - 1

reversed_str = ''

while ln >= 0:
    reversed_str  = reversed_str + get_input[ln]
    ln = ln - 1

if  get_input ==  reversed_str :
    print('Input string is palidrome')
else:
    print('Input string is not palidrome')


#how to find if there is mutiple occurnce of same value in list/string/tuple.
print('How to find if there is mutiple occurnce of same value in list/string/tuple')

l1 = ["eat", "sleep", "repeat" , "eat","eat"]

result = ''
get_str = input('Enter the word to find position :')

for i in range(0,len(l1)):
    print(i ,l1[i])
    if get_str == l1[i]:
        if result == '':
           result = str(i)
        else:
           result = result + ',' + str(i)

print(result)


print('Finding String contains same words position')
strresult = ''
findwords = 'eat, sleep, repeat, eat'
print('Counting words')
count = 0
for i in findwords.split(','):
    print(i)
    if get_str == i.strip():
       if strresult == '':
          strresult = str(count)
       else:
          strresult = strresult + ',' + str(count)
    count += 1

print(f'string {get_str} = {strresult}')


print('Using tuple to find same words position')
str1 =  ("eat", "sleep", "repeat" , "eat")
result1 = ''
for i in range(0,len(str1)):
    if get_str == str1[i]:
       if result1 == '':
          result1 = str(i)
       else:
         result1 = result1 + ',' + str(i)

print(f'Using tuple method to find position of words = {result1}')


l1 = ["eat", "sleep", "repeat",'eat']
print('Finding same words position using enumerate')
print(list(enumerate(l1))[0][0])

# printing the tuples in object directly
rs = ''
for ele in enumerate(l1,1):
    if get_str == ele[1] :
        if rs == '':
            rs = str(ele[0])
        else:
           rs = rs + ','+ str(ele[0])
print(f'using enumerate function the  result is = {rs}')

import enchant
d = enchant.Dict("en_US")
print(d.check('Hello'))


print('Find give two string are annagrams or not ')
import random
str1 = "save"
str2 = "vase"
if sorted(str1) == sorted(str2) :
    print('Given strings are annagrams')
else:
    print('Gien string is not annagrams')
'''    
new_str = []
new_str1 = []
for i in str1:
    new_str.append(i)
count = 0


for i in range(len(new_str)):
     new_str.insert(i+1,new_str.pop(i))

     print(new_str)
count +=1
'''


#new_str = asve,avse,aves ,vsae,vase,vesa


'''
Filter() is a built-in function in Python. 
The filter function can be applied to an iterable such as a list or a dictionary 
and create a new iterator. This new iterator can filter out certain specific elements 
based on the condition that you provide very efficiently. 

Note: An iterable in Python is an object that you can iterate over.
      It is possible to loop over an iterable and return items that are in it.

Python filter() with the lambda expression is the most used way to filter the elements 
from the iterable like set, list, tuple, and dictionary.

'''

l1 = ["eat", "sleep", "repeat",'eat']
dict = dict(filter(lambda x:l1.count(x[1]) > 1, enumerate(l1)))
print(dict.keys())


