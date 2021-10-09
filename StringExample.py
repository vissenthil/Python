Name ='Senthil Kumar'
print(Name.split()) # split by space
print(Name.split('l')) # split after the charactor
print(Name.count('m'))
l ='abcddefgghhhhhjjassbdd'
print(l.count('d'))
Name = '           senthil kumar        '
print(Name.strip()) # remove white space left and right side not between the words
print(Name.lstrip()) # remove white space left side only like ltrim in oracle
print("*".join("senthil kumar")) # join * between each charactor
print("*".join(Name)) # join * between each charactor
x = 'sunday'
print(x.capitalize())
print(Name.upper())
print(Name.lower())
print(x.center(30,'x')) # center x values between 30 and it allows only single charactor or space
print(x.center(30,' ')) # center x values between 30 and it allows only single charactor or space
print(x.isupper()) # it will return boolean value True or False
print(x.islower()) # it will return boolean value True or False
print(x.isdigit()) # it will return boolean value True or False
Name ='ThalirSenthilKumar'
rname =''
l = len(Name)
while l > 0:
    l-=1
    rname+=Name[l]
print('Revarsed Name is:',rname)

# String formate
name = input('Please enter your Name:')
fatherName = input('Enter you father Name:')
Age = input('Enter your age :')
finalresult = 'My Name is {} and my father name is {} my age is {}'.format(name,fatherName,Age)
print(finalresult)
# anoter way
print(f'My Name is {name} and my father name is {fatherName} my age is {Age}')