
def Find_Palindrome(Str):
    ''' This function will check the given string
        are palindrome or not '''
    ln = len(Str) - 1

    reversed_str = ''

    while ln >= 0:
        reversed_str  = reversed_str + get_input[ln]
        ln = ln - 1

    if  Str ==  reversed_str :
        print('Input string is palidrome')
    else:
        print('Input string is not palidrome')

def Count_same_word_position(str2):
    # how to find if there is mutiple occurnce of same value in list/string/tuple.
    print('''How to find if there is mutiple occurnce of same value in list
            as shown below ''') #/string/tuple')
    l1 = ["eat", "sleep", "repeat", "eat", "eat"]
    result = ''
    for i in range(0, len(l1)):
        print(i, l1[i])
        if str2 == l1[i]:
            if result == '':
                result = str(i)
            else:
                result = result + ',' + str(i)
    print(f'The word {str2} appear in the list in position {result}')


def same_word_position_in_string(str3):
    ''' This function find out same word appear in multiple positions'''
    print('Finding String contains same words position')
    strresult = ''
    findwords = 'eat, sleep, repeat, eat'
    print('Counting words')
    count = 0
    for i in findwords.split(','):
        print(i)
        if str3 == i.strip():
            if strresult == '':
                strresult = str(count)
            else:
                strresult = strresult + ',' + str(count)
        count += 1

    print(f'The word {str3} appear in the string in {strresult} positions')


def same_word_position_in_tuple(str4):
    print('\nUsing tuple to find same words position')
    str1 = ("eat", "sleep", "repeat", "eat")
    result1 = ''
    for i in range(0, len(str1)):
        if str4 == str1[i]:
            if result1 == '':
                result1 = str(i)
            else:
                result1 = result1 + ',' + str(i)

    print(f'Using tuple method to find position of words = {result1}')


def enum_method_find_word_postion(str5):
    l1 = ["eat", "sleep", "repeat", 'eat']
    print('\nFinding same words position using enumerate')
    print(list(enumerate(l1))[0][0])

    # printing the tuples in object directly
    rs = ''
    for item in enumerate(l1, 1):
        if get_str == item[1]:
            if rs == '':
                rs = str(item[0])
            else:
                rs = rs + ',' + str(item[0])
    print(f'using enumerate function the  result is = {rs}')

def find_annagram(str1,str2):
    print('\nFind give two string are annagrams or not ')
    str1 = "save"
    str2 = "vase"
    if sorted(str1) == sorted(str2) :
        print('Given strings are annagrams')
    else:
        print('Gien string is not annagrams')


def enum_to_find_word_position():
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

    l1 = ["eat", "sleep", "repeat", 'eat']
    dict1 = dict(filter(lambda x: l1.count(x[1]) > 1, enumerate(l1)))
    print(f'\nWord position in the list using enumerate is :{dict1.keys()}')



if __name__ == '__main__':
    get_input = input('Please enter any string to find palindrome or not :')
    Find_Palindrome(get_input)
    get_str = input('\nEnter the word to find position :')
    Count_same_word_position(get_str)
    same_word_position_in_string(get_str)
    enum_method_find_word_postion(get_str)
    print('\nPlease enter two strings to find annagrams:-')
    str1 = input('Enter a first string :')
    str2 = input('Enter a first string :')
    find_annagram(str1,str2)
    enum_to_find_word_position()






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





