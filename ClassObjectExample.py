#class and Objects in python
import random

print(''' How to create a Class Syntax: class className:
          Here test is a class name. Each function created
          inside a class must have a parameter(it is pointer)  then only class will know
          it has a function within it.
          
          How to call a function inside a class :
             First we need to create a class variable(object) and call the 
             function Example:-
                  a = test.MyFirstClass()''')

class test:
    def MyFirstClass(self):# here self is a pointer it can be any name may be your name
        print("My First Class in python")
a = test()
print(a.MyFirstClass())

class Test1:
    def __init__(self,a,b,c): # This a method will be called by defaule each time whe the class method is called.
        self.a1 = a # Here self.a1 is class object or class variable,a,b,c are the parameters
        self.b1 = b
        self.c1 = c
    def SumTest(self): # it is class method used to sum all the values
        return self.a1 + self.b1 + self.c1
                   # Here we can not use selt.a + self.b + self.c because it class will not know this
                   # we can access only class varibale inside the class
b = Test1(10,20,45) # Creating class variable and it has three paramters and it need to be provided
                    ## when the new object is created. We can create number new objects with different parameters
print(b.SumTest())
c = Test1(3,2,6)
print(c.SumTest())

class Test3:
    def CreatAccount(self):
        self.Name = input('Please Enter Account holder Name:')
        self.Sex  = input('Please endter Sex:')
        self.AccountNo = random.randint(1,1000)
        print(self.AccountNo)
        self.depositAmount = int(input('Please enter the deposit Amt:'))
    def DisplayAccountDetails(self):
        print('Your Account Has been Created:')
        print(f'Account Holder Name:{self.Name}')
        print(f'Account Number     :{self.AccountNo}')
        print(f'Sex                :{self.Sex}')
        print(f'Deposited Amount   :{self.depositAmount}')
AccountInfo = Test3()
AccountInfo.CreatAccount()
AccountInfo.DisplayAccountDetails()

def CreateAccount():
    ContinueFlag = True
    while ContinueFlag:
        AccountInfo.CreatAccount()
        ans = input('Do you want to Continue Y/N:')
        if ans == 'N' or ans == 'n':
            ContinueFlag =False
CreateAccount()