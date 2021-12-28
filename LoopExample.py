L = [1,2,3,'SENTHIL']
for i in L :
    print(i)
else:
    print('On Sucess') # execute at the end of complete if break used in bewteen it will not excute

i = 1
n = 5
while i < n :
    print(i)
    i +=1
else:
    print('On Sucess')
i = 1

while i < 10 :
    print(i)

    if i == 5:
        break
    i += 1
else:
    print('On sucess') # will not print beacuse it will print only while complete itself here we do break forcefully
                       # so it wont print the else part

Name = 'Senthil Kumar'
for i in Name :
    print(i)
    if i == 'h':
        break
else:
    print('Completed sucessfuly') # it wont work beacuse not normal completion

i = 4
n = 10
while i < n :
    print(i)
    if i == 6 :
        continue # if i = 6 it will continue it won't execute after the continue statement
                 # it will not come to increment part so it will be infinitive
    i+=1

