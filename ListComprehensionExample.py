mystring = 'Hello Every One'
print(mystring)
print('Example of list comprehension:-')
mylist = [letter for letter in mystring]
print(mylist)
mylist = [x for x in 'senthilkumar']
print(mylist)
mylist = [1,2,3,4,5,6]
oddnum,evenNum = [[x for x in mylist if x%2 == 0],[y for y in mylist if y%2 != 0]]
print(f'Odd Number in the List is {oddnum} and Even Number is{evenNum}')
mylist = [ num for num in range(0,18)]
print(mylist)
mylist = [ num*2 for num in range(0,18)]
print(mylist)
mylist = [ num**2 for num in range(0,18)]
print(mylist)
celcius = [10,34,56.5,100]
farenhit = [((9/5)*temp+32) for temp in celcius]
print(farenhit)
print('Using if else stament inside list comprehension:-')
result = [x if x%2 == 0 else "Odd" for x in range(0,100)]
print(result)
print('Nexted loop inside list comprehension')
mylist = [x*y for x in [1,3,4,5] for y in [10,100,300,400]]
print(mylist)

print('List comprehension to print the range of 1 to 50 that are divisable by 3')
divisableBYThree = [ x  for x in range(1,50) if x%3 == 0  ]
print(divisableBYThree)
print('Go through the list the words in this sentence and print if the lenth of the letters is "even"')
evenWords = 'Go through the list the words in this sentence and print if the lenth of the letters is "even"'
listofEvenWords = [x for x in evenWords.split() if len(x)%2 == 0]
print('words length is{0} Even word is{1}'.format(len(listofEvenWords),listofEvenWords))
mylist =[(x if x%3 == 0 else 'Fizz') if x%5 == 0 else 'Buzz'  for x in range(1,100)]
print(mylist)
word = 'print only the words that start with s in the sentence'
for words in word.split():
    if words.startswith('s'):
        print(words)
#if words.startswith('s'):

print(word.split())
print('Use a list Comprehension to create a list of the first letters of every word in the string below')
st ='Create a list of the first letters of every word in this string'
print(st)
EachWrod = [word[0] for word in st.split()]
print(f'list of first letters is:{EachWrod}')
print(help(list.insert))