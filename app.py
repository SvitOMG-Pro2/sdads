from calendar import c
from distutils.log import error
import os


password = 'HI'

x = 44
y = 5

somting = False
a = x/y
c = x%y
i = int(x / y)
while True:
    inp = input('Command: ')
    if inp == '/sudo mode dev ' + password:
        somting = True
        print('you aceved Creative mode, hi Elon Musk')

    if inp == '/sudo cls':
        print('Ok, Ok, am cleaning...')
        os.system('cls')





    if inp == 'a':
        print(a)
    elif inp == 'x':
        print(x)
    elif inp == 'y':
        print(y)
    elif inp == 'c':
        print(c)
    elif inp == 'i':
        print(i)
    else:
        print('Input isent an verable or any known command, you writed' + inp)
#        while somting == True:
        if error and somting == True:
            print(error)


    
