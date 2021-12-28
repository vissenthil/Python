

def GetInput():
    L = []
    Again = True
    while Again:
        try:
            val = int(input('Please enter integer:'))
            if val <=3:
                raise  Exception('Value should not be less then :',val)
            if type(val) == int:
                L.append(val)
            if type(val) != int:
                Again = True
            if len(L) >=5:
                Again = False
                print(L)
        except Exception as e:
            print(e)

GetInput()