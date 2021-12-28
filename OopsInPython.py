
class person:
    def __init__(self,name,surname,year_of_birth):
        self.name = name
        self.surname = surname
        self.year_of_birth = year_of_birth
    def age(self,CurrentYear):
        return CurrentYear - self.year_of_birth

senthii = person('Senthilkumar','S',1975)
myage = senthii.age(2021)
print(myage)

print('Inheritence accessing parent class properties by use of inheritance here person is parent class')
class student(person):
    def __init__(self,sudentid,*args): # Here *args means to access all the variables name,surname,year_of_birth
                                       # from the parent class person. we use *args otherwise need to use all here
        self.sudentid = sudentid
        super(student, self).__init__(*args)    # super means to initialize person class
                                                # we can use super or person.__init__()
student1 = student(234,'Ramu','K',1990)
student1.age(2021)
print(f'Sudtent {student1.name} age is {student1.age(2022)}')
print('Multiple inheritance Example')
class test:
    def __init__(self,a,b):
        self.a = a
        self.b = b
class test1:
    def __init__(self,c,d):
        self.c = c
        self.d = d
print('If we inherit parent class we need to re-initialise in the child class otherwise we can not use objecs'
      'of parent class in the child class')
class child(test,test1): # Inheriting both classes
    def __init__(self,*args):
        test.__init__(self,*args)
        test1.__init__(self,*args)
    def func_child(self):
        print(self.a,self.c)

childObj = child(34,67)
print(childObj.func_child())
print('''Here we are trying to print a value from test class and c values from test1
      it shows the same values because it is passing save values to both classes because of using *args''')
class test:
    def __init__(self,a,b):
        self.a = a
        self.b = b
class test1:
    def __init__(self,c,d):
        self.c = c
        self.d = d

print(''' Here we are initializing actual variable name instead of *args
         we need to pass all variables values while creating child object
         it will pick up the correct values from class object and shows.''')
class child(test,test1): # Inheriting both classes
    def __init__(self,a,b,c,d):
        test.__init__(self,a,b)
        test1.__init__(self,c,d)
    def func_child(self):
        print(self.a,self.c)

childObj = child(34,67,56,100)
print(childObj.func_child())

print('Eample of multi label inheritance:-')

class P1:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def P1_Func(self):    
        print('This is come from P1 Method')
class P2(P1):
    def __init__(self):
        pass
    def P2_Func(self):
        return  'This is from class P2'

class child(P2):
    def __init__(self):
        pass
    def Child_Fun(self):
        return  'This is come from Child class'

multiObject = child()
print(multiObject.P2_Func())
print(multiObject.Child_Fun())
print('No need to initialise each class if your not going to until '
      'ur not going to use the variable inside the class ')
class P1:
    def P1_Func(self):
        print('This is come from P1 Method')
class P2(P1):
     def P2_Func(self):
        return  'This is from class P2'

class child(P2):
     def Child_Fun(self):
        return  'This is come from Child class'
multiObject = child()
print(multiObject.P2_Func())
print(multiObject.Child_Fun())
print('Example for Method Overloading')
class person:
    def __init__(self,name,surname,yearOfBirth):
        self.name = name
        self.surname = surname
        self.yearOfBirth = yearOfBirth
    def age(self,CurrentYear):
        return self.yearOfBirth - CurrentYear
    def __str__(self): # it is function will print when we call the class object by defult
        return  self.name

per = person('senthil','Vi.S',1076)
print(per)
print(per.surname)

class person:
    def __init__(self,name,surname,yearOfBirth):
        self.name = name
        self.surname = surname
        self.yearOfBirth = yearOfBirth
    def age(self,CurrentYear):
        return self.yearOfBirth - CurrentYear
    def __str__(self): # it is function will print when we call the class object by defult
        return  self.name

class student(person):
    def __init__(self,studentId,*args):
        super(student, self).__init__(*args)
        self.studentId = studentId

    def FullName(self):
        return self.surname + ' ' +  self.name
    def __str__(self):
        ##return  self.FullName()
      # return self.name + 'his id is:' + str(self.studentId)
      # using __str__ method from parent class
       return  super(student, self).__str__() + 'his id is:' + str(self.studentId)

chilObj = student(1223,'Aruthra','S',2015)
print(chilObj)
print( chilObj.FullName())
'''class test:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b

class test1(test):
    def __init__(self,c,d):
        self.c = c
        self.d = d
        test1.__init__(*args)
    def multiplication(self):
        return self.a * self.d

class test3(test1):
    def __init__(self,a,b,c,d):
       super(test3, self).__init__(self,a,b,c,d)

multLabelObj = test3(1,2,3,4) '''

class tyre :
       def __init__(self,branch,belted_bais,opt_pressure):
           self.branch = branch
           self.belted_bais = belted_bais
           self.opt_pressure = opt_pressure
       def __str__(self):
           return self.branch + ' ' + self.belted_bais + ' ' + self.opt_pressure
class engine:
      def __init__(self,fuel_type,noise_level):
          self.fuel_type = fuel_type
          self.noise_level = noise_level

      def __str__(self):
          return  self.fuel_type + ' ' + self.noise_level
class body:
    def __init__(self,size):
        self.size = size
    def __str__(self):
        return self.size

class car:
    def __init__(self,a,b,c):
         self.a = a
         self.b = b
         self.c = c
    def __str__(self):
        return self.a + self.b + self.c

objtyre = tyre('branch','belted_bais','opt_pressure')
print(objtyre)
objEngine = engine('fuel_type','noise_level')
print(objEngine)
objBody = body('size')
print(objBody)
objcar = car('a','b','c')
print(objcar)
objcar = car(str(objtyre),str(objEngine),str(objBody))
print(objcar)

class Mulitiplication:
     def __init__(self,a):
         self.a = a
     def __mul__(self, other):
         return self.a * other.a
b = Mulitiplication(4)
a = Mulitiplication(4)
print(a * b)