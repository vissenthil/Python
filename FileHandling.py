import os

def create_file(filename,text):
    try:
        with open (filename,'w') as f:
            f.write(text)

    except IOError:
        print(f'Problem in  writing to  {filename}  file')

def read_file(filename):
    try:
        with open(filename,'r') as R:
            readedtext = R.read()
        print(f'Text Readed from file is: {readedtext}')
    except IOError:
        print(f'Unable to read from {filename}')


def update_file(filename,text):
    try:
        with open(filename,'a') as A:
            A.write(text)
        print('New text has been updated successfully')
    except IOError:
        print('Unable to update file')

def delete_file(filename):
      try:
        os.remove(filename)
        print('File has been deleted successfully')
      except IOError:
         print('Unable to delete the file')

def rename_file(filename,newfilename):
     try:
       os.rename(filename,newfilename)
       print(f'file {filename} changed to {newfilename} successfully!!!!!')
     except IOError:
        print('Error:Unable to rename a file.')

if __name__ == '__main__':
    Fname = input('Please enter a file name :')
    Wtext = input('Enter the text to write into file:')
    create_file(Fname,Wtext)
    read_file(Fname)
    New_text = input('Please enter new text to update in file:')
    update_file(Fname,New_text)
    print('Updated text in the file is:')
    read_file(Fname)
    delete_file(Fname)
