
print("  ********************* String example in Python ****************************")
print('What is a String?')
print('A string is a sequence of characters.')
print('How to create a string in Python?')
print('''Strings can be created by enclosing characters inside a single quote or double-quotes. 
        Even triple quotes can be used in Python but generally used to represent multiline strings 
        and docstrings.''')
print('Example1  a = "this is a example for string" ')
print("Example2  a = 'this is example for string' ")
print("Example3  a = '''this is example for string''' ")
print('How to access characters in a string?')
print('''We can access individual characters using indexing and a range of characters using slicing. 
        Index starts from 0.''' )
GetString = input('Enter a string :')
GetIndexPos = int(input('Enter a index posion to print the character - will start with at the end:'))
print(f'Character at {str(GetIndexPos)} is:',GetString[GetIndexPos])
print('Example range of characters using slicing:-')
GetString = input('Enter a string :')
GetIndexstart = int(input('Please enter start index:'))
GetIndexend   = int(input('Please enter start index:'))
print(f'Range of characters between  {str(GetIndexstart)} : {str(GetIndexend)} is:',GetString[GetIndexstart:GetIndexend])

print('''If we try to access an index out of the range or use numbers other than an integer, 
         we will get errors.''')
GetString = input('Enter a string :')
GetIndexPos = int(input('Enter a index posion to print the character - will start with at the end:'))
print('Character at position is:',GetString[GetIndexPos])

print('''Strings are immutable. This means that elements of a string cannot be changed once they have been assigned. 
      We can simply reassign different strings to the same name.''')
print( 'Example a = "Senthilkumar" ')
print(' a[1] = "T"  TypeError: "str" object does not support item assignment ')
print( ''' possible a = "Senthil Kumar"
       b = a 
       now a will hold "Senthil kumar" ''')
print('''We cannot delete or remove characters from a string. 
        But deleting the string entirely is possible using the del keyword.''')
print(''' Example del my_string[1]
         TypeError: 'str' object doesn't support item deletion''')
print('''Possible del my_string will allow to delete hole string''')
getstring = input('Enter a string to use del methond to delete the string:')
print('Use del string variable name to delete the hole string')
del getstring
print('String is deleted..........')
print(''' Concatenation of Two or More Strings
         Joining of two or more strings into a single one is called concatenation.
        The + operator does this in Python. Simply writing two string literals together also concatenates them.''')
GetStr1 = input('Enter first string:')
GetStr2 = input('Enter first string:')
print('Firtst string is :',GetStr1)
print('Firtst string is :',GetStr2)
print( 'Concatenation of two string is :', GetStr1 + GetStr2)
print('The * operator can be used to repeat the string for a given number of times.')
print('Example  "Hello" * 3')
print('hello ' * 3)
print('Writing two string literals together also concatenates them like + operator.')
print('Exampl3e "HELLO" "SENTIL"')
Getstring = input('Please enter two string at same line with single quotes:')
print('Concatenates string is:',Getstring)

print('Iterating Through a stringWe can iterate through a string using a for loop')
Getstring = input('Please enter a string:')
countChar = input('Enter a charactor to count in the entered string:')
count = 0
for letter in Getstring:
    if letter == countChar:
        count +=1
print('Count of character in the string is:',count)

print('''String Membership Test
        We can test if a substring exists within a string or not, using the keyword in.''')
Getstring = input('Please enter a string :')
GetInstr = input('Enter a word to check if that word exists or not:')
print('Word exists yes means true no means Fale :', GetInstr in Getstring)
print('Various built-in functions that work with sequence work with strings as well.')

print('The enumerate() function returns an enumerate object. It contains the index and value of all the items in the string as pairs. '
      'This can be useful for iteration.')
print('Example of enumerate function for :',Getstring)
print(list(enumerate(Getstring)))
print('The len(str) returns the length (number of characters) of the string.')
Getstring = input('Enter a string to know the length of that string:')
print('Length of entered string is:',len(Getstring))

print('''The format() Method for Formatting Strings:-
         The format() method that is available with the string object is very versatile and powerful 
         in formatting strings. Format strings contain curly braces {} as placeholders or replacement 
         fields which get replaced. We can use positional arguments or keyword arguments to specify the 
         order.''')
print('''For example default(implicit) order: default_order = "{}, {} and {} {}".format('senthil','thalir','aruthra','krithi')''')
default_order = "{}, {} and {} {}".format('senthil','thalir','aruthra','krithi')
print(default_order)
print('''Exmaple for order using positional argument positional_order = "{1}, {0} and {2} {3}".format('senthil','thalir','aruthra','krithi')''')
positional_order = "{1}, {0} and {2} {3}".format('senthil','thalir','aruthra','krithi')
print(positional_order)
print('''Example for order using keyword argument: keyword_order = "{s}, {t} and {a} {k} ".format(s = 'Senthil',t = 'Thalir',a = 'Aruthra', k = 'Krithi' )''')
keyword_order = "{s}, {t} and {a} {k} ".format(s = 'Senthil',t = 'Thalir',a = 'Aruthra', k = 'Krithi' )
print(keyword_order)


print('**********************Python String Methods**************************************')
print(''' 1. casefold()               11. isalnum()
          2. capitalize()             12. isalpha()
          3. casefold()               13. isdecimal()
          4. center()                 14. isdigit()
          5. count()                  15. isidentifier()
          6. title()  
          7. startswith()
          8. endswith()  
          9. find() 
          10 index()''')
print('''str.upper() Return a copy of the string with all the cased characters converted to uppercase.''')
a = input('Enter a lower case string to do upper case:')
print(a.upper())

print('''str.lower() Return a copy of the string with all the cased characters converted to lowercase.''')
a = input('Enter a upper case string to chnage to lower case:')
print(a.lower())
print('''str.swapcase()
Return a copy of the string with uppercase characters converted to lowercase and vice versa.''')
name = input('Please enter you name to swapsase:')
print(name.swapcase())
print(''' str.title()
        Return a titlecased version of the string where words start with an uppercase 
        character and the remaining characters are lowercase.''')
EnterSentence = input('Enter a line of string to test titlecase :')
print(EnterSentence.title())

print('''str.zfill(width)
        Return a copy of the string left filled with ASCII '0' digits to make a string of length width. 
        A  leading sign prefix ('+'/'-') is handled by inserting the padding after the sign character 
        rather than before. The original string is returned if width is less than or equal to len(s).''')
num = input('Eter numebrs to check zfill methods of str:')
a   = int(input('Enter number of digits to fill with:'))
print(f'{num} is filled with '+ str(a) + ' length of digits',num.zfill(a))
num = input('Eter numebrs with + or -  to check zfill methods of str:')
print(f'{num} is filled with '+ str(a) + ' length of digits',num.zfill(a))
print(''' str.strip([chars])
        Return a copy of the string with the leading and trailing characters removed. 
        The chars argument is a string specifying the set of characters to be removed. 
        If omitted or None, the chars argument defaults to removing whitespace''')
print("'        senthilkumar         '")
print('After str.strip()')
print('        senthilkumar         '.strip())
strTosTrip = input('Enter a to check strip method example "www.google.com" :')
removecharacters = input('Enter a list of charactors to be remove "Exampele womzc." : ')
print(f"{strTosTrip} after strip('womzc.') it reomves a specified characters \n",strTosTrip.strip(removecharacters))
print('''str.startswith(prefix[, start[, end]])
        Return True if string starts with the prefix, otherwise return False. 
        prefix can also be a tuple of prefixes to look for. With optional start, 
        test string beginning at that position. 
        With optional end, stop comparing string at that position.''')
wordtocheck = input('Please enter a sentence to check startwith:')
ans = input('Ener a word to check it is start with the sentence you typed:')
print(f'Sentence start with {ans}?:',wordtocheck.startswith(ans))
wordtocheck = input('Please enter a sentence to check Endswith:')
ans = input('Ener a word to check it is ends with the sentence you typed:')
print(f'Sentence Ends with {ans}?:',wordtocheck.endswith(ans))