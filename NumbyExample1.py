import  numpy as np
print('Create array using np.arrary Method')
ar1 = np.array([[1,2,],[3,4]])
print(ar1)
ar2 = np.array([1,2,3],ndmin=3) # here ndmin= 3 meands three dimentional array show three [[[ ]]]
print(ar2)
ar3 = np.array([[1,2],[3,4]])
print(ar3)
# ar3[row][columm]
print(ar3[1][1])
#we can also acess using ar3[row,column]
print(ar3[1,0])
print('Create floating point array by using dtype = np.float64')
arr4 = np.asarray([1,2,3,4],dtype=np.float64)
print(arr4)
print('Create integer array by using dtype = np.int32')
arr4 = np.asarray([1,2,3,4],dtype=np.int32)
print(arr4)
print('''np.asanarray will create array formate if the given input is not in the array formate,
      it will convert into array, if it is in a array formate it will not conver into array''')
arr5 = np.asanyarray([1,2,3,4,5])
print(type(arr5))
print(arr5)
arr6 = np.asanyarray(np.mat([1,2,3,4]))
print(type(arr6))
print(arr6)
print('Create arry using np.fromfunction methods')
print(''' Here shape means dimension of array 3,4 matrix array 3 rows and 4 columns
    ''')
print('Using multiplication ')
arr7 = np.fromfunction(lambda i, j : i * j ,dtype=np.int32,shape=(3,4))
print(arr7)
print('Using addition operation')
arr7 = np.fromfunction(lambda i, j : i + j ,dtype=np.int32,shape=(3,4))
print(arr7)
print('''Here in the below example shape(3,4,2) meamns shape(3array,4rows,2colums)
totaly 3 array each with 4rows and 2columns. 3 dimentional array''')
arr7 = np.fromfunction(lambda i, j,k : i + j + k ,dtype=np.int32,shape=(3,4,2))
print(arr7)
print(arr7[1][2,1])
print('Example of arry creating arry with help of np.fromiter method')
arr8 = np.fromiter([1,2,3,4,5,6],dtype=np.float32)
print(arr8)
print('''Example of arry creating arry with help of np.fromstring method
it will not crate arry with strings but string of numbers it will create''')
arr9 = np.fromstring('4343 545454 756565 75567',sep= " ")
print(arr9)
print('To know the dimension of array use np.ndim function')
print(arr9.ndim)
print('To know the size of an array user np.size it will give the total number of element in the array')
print(arr9.size)
print('Use np.shape to know the number of rows and colums of the array')
print(arr9.shape)
print('Range function accept only int value as lower and upper values it will not allow floating values')
l = list(range(0,10))
print(l)
#l = list(range(0,6.5)) # Error due to floating point value
#print(l)
print('Using np.arange function which allows the floating point values')
l = np.arange(0,5.6)
print(l)
print('Creating arry using np.linspace method by default it will create 50 element')
linspace = np.linspace(1,10)
print(linspace)
linspace = np.linspace(1,10,5) # here 5 means totaly 5 elements by defulat it is 50 element.
print(linspace)
linspace = np.linspace(1,10,10) # here 5 means totaly 10 elements by defulat it is 50 element.
print(linspace)
print('Creating arry using np.zero')
ZeroArray = np.zeros(5)
print(ZeroArray)
print('zero array with 4 * 5 matrix')
ZeroArray = np.zeros((4,5))
print(ZeroArray)
print('Creating arry using np.ones')
OneArray = np.ones(10)
print(OneArray)
print('Ones array with 4 * 5 matrix')
OneArray = np.ones((4,5))
print(OneArray)
print('Adding 2 with each elements of ones array ')
print(OneArray)
print('Creating arry using np.empty() method which will create random element each time excute it will create'
      'random element')
EmptyArr = np.empty((2,2))
print(EmptyArr)
print('Creating array using np.eye methods')
EyeArray = np.eye(5)
OneArray = np.ones((4,5)) + 2
print(EyeArray)
print('Create arry using np.random.rand method here 10 rows 5 columms')
RandomRand = np.random.rand(10,5)
print(RandomRand)
print('Create arry using np.random.rand method here 10 arrys with 5rows and 3 columms')
RandomRand = np.random.rand(10,5,3)
print(RandomRand)
print('Create arry using random.rantint')
print('''Here random.randint(startpoint,endpoint,size) it will create randon integer values between start to end for the
 mentioned size here size = 50''')
RandomRantIntAr = np.random.randint(3,100,50)
print(RandomRantIntAr)
print(''' np.random.randint(1,6,(3,4)) hrere starting  1 to 6 , 3 rows and 4 column array will be created.''')
RandomRantIntArr = np.random.randint(1,6,(3,4))
print(RandomRantIntArr)
print('Array shape to know the array size use ArrayName.shape method Example: RandomRantIntArr.shape')
print(RandomRantIntArr.shape)
print('Reshape the array into another shape using ArraryName.reshpae ')
#RandomRantIntArr.reshape(1,3,4)
print(RandomRantIntArr.reshape(6,2))
#RandomRantIntArr.reshape(4,3)
print('After reshape')
print(RandomRantIntArr)
print('After reshape RandomRantIntArr.reshape(4,3) reshape can be done only with in the actual shape of the array')
print(RandomRantIntArr.reshape(4,3))
print('How to get the maximum array element: ArrayName.max()')
print(RandomRantIntArr.max())
print('How to access array element : ArrayName[row,column]')
print(RandomRantIntArr[0,2])
print('How to change the array element: ArrayName[row,column]= newvalue ')
RandomRantIntArr[1,1] = 234
print(RandomRantIntArr)
print('Matrix Multiplication :-')
Matrix1 = np.random.rand(3,3)
Matrix2 = np.random.rand(3,3)
Matrix3 = Matrix2 * Matrix1
print(Matrix1)
print(Matrix2)
print('Matrix Multiplication of two matrix elementwise is :')
print(Matrix3)
Matrix1 = np.random.randint(2,6,(3,3))
Matrix2 = np.random.randint(1,3,(3,3))
print(f' Matrix1 =  {Matrix1}')
print(f'Matrix2 = {Matrix2}')
print('''Matrix mulitplication we have to use @ symbol if we 
         use * it will producee elementwise multiplication
         not a matrix multiplication. mulitiplication will be applied
         as first martrix row value will be multiplied by secondmatrix each colume value''')
print(Matrix1 @ Matrix2)
print('Transpose of matrix:ArrayName.T Will transpose the matrix')
print(Matrix1)
print('Transpose of Matrix1.T')
print(Matrix1.T)
print('Power of each element user ArrayName **2')
print(f'Matrix1) ={Matrix1}')
print('Power of Matrix1 is:')
print(Matrix1 **2)
print('Exponse of Martix1 is:')
print(f'Matrix1) ={Matrix1}')
print(np.exp(Matrix1))
print('Log of Matrix1 is:-')
print(f'Matrix1) ={Matrix1}')
print(np.log10(Matrix1))
print('SqureRoot of each element of Matrix1 is:-')
print(f'Matrix1) ={Matrix1}')
print(np.sqrt(Matrix1))
print('pi value ')
print(np.pi)