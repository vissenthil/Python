
pirnt('Program to ask user input again and again in not a inter value')

def askinput():
    again = True
    while again:
        try:
            a = int(input('Please enter interger value:'))
            if type(a) != int:
                again = True
                print('Making True')
            if type(a) == int:
               print(a/10)
               print('Making False')
               again = False
        except Exception as e:
            print(e)
askinput()
# simple method to ask again and again if not interger values is not given

def GetInput():
    try:
        val = int(input('Kindly enter integer value'))
    except Exception as e:
        GetInput()


GetInput()

def GetUserInput():
    print('This is from GetUser Input Function')
    while True:
        try:
            val = int(input('Give Integer value'))
        except Exception as e:
            print('There is an Error:',e)
            continue
        else:
            break
        finally:
            print('All good finaly')

GetUserInput()