
import numpy as np
import functools as ft # reduce function is available in this module so we are importing here

l = [1,2,3,4,5,6,7]

def test(data):
    return data + 1
# map takes two arguments first one as function, second one is iterable
print(help(map))
l2 = list(map(test,l))
print(l2)

def test1(data):
   if data <4:
       return  data **3
   else:
       return np.log(data)
l3 = list(map(test1,l))
print(l3)
print(help("lambda"))
l4 = list(map(lambda x : x+1, l))
print('using lambda fucntion')
print(l4)
print('Lambda with multiple arguments Example')
l1 = [1,2,3,4,5,6]
l2 = [13,22,37,42,65,66]
l3 = list(map(lambda x,y : x+y,l1,l2))
print(l3)
print('if else inside lambda function example:-')
l4 = list(map(lambda x : np.sqrt(x) if x < 4 else np.log(x) ,l))
print(l4)
l1 = [1,2,3,4,5,6]
def test(x,y):
    return x+y
print('Reduce function takes two arguments and make aggregate or sum all the values will return one value')
l5 = ft.reduce(test,l)
print(l5)
print('Redue using lambda function:-')
l6 = ft.reduce(lambda x,y : x+y,l)
print(l6)
l7 = ft.reduce(lambda x,y : x if x > y else y,l)
print(l7)
l = [1,4,3,5,7,2,6,89,22,45,67,20]
l8 = list(map(lambda x : True if x%2 == 0 else False,l))
print(l8)
print('Using filter function:-')
print('To pring even numbers using filter function')
def test(data):
    if data %2 == 0:
        return  True
    else:
        return False

L9 = list(filter(test,l))
print(L9)
print('Filter function using lambda:-')
l10 = list(filter(lambda x : True if x%2 == 0 else False,l))
print(l10)
