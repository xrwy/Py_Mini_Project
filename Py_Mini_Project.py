import os 
import sys
import sqlite3 


dataAdd = []


def getInformations():
    name = str(input('Enter Name :'))
    if name == '':
        print('Do not leave the fields blank.')
    dataAdd.append(name)
                
    surname = str(input('Enter Surname :')) 
    if surname == '':
        print('Do not leave the fields blank.')
    dataAdd.append(surname)

    age = int(input('Enter Age :')) 
    if age == '':
        print('Do not leave the fields blank.')
    dataAdd.append(str(age))
                
    number = int(input('Enter Number :')) 
    if number == '':
        print('Do not leave the fields blank.')
    dataAdd.append(str(number)) 
                
    country = input('Enter Your :')  
    if country == '':
        print('Do not leave the fields blank.')
    dataAdd.append(country)  


def inforationSave():
    with sqlite3.connect('persons.db') as persons:
        personsCursor = persons.cursor()
        personsCursor.execute('''CREATE TABLE IF NOT EXISTS person(id_ INTEGER PRIMARY KEY,name TEXT,surname TEXT,age TEXT,number TEXT,country TEXT)''')
        personsCursor.execute('''SELECT * FROM person''')
        data = personsCursor.fetchall()
        if data == []:
            personsCursor.execute('''INSERT INTO person(name,surname,age,number,country) VALUES(?,?,?,?,?)''', dataAdd)
            persons.commit()
            choose()
        else:
            sql = '''SELECT *  FROM person WHERE number = ? '''
            personsCursor.execute(sql, (dataAdd[3],))
            data = personsCursor.fetchall()
            if len(data) == 1:
                print('Pre-Registered. Change the information and login again.')
                exit()
            else:
                personsCursor.execute('''INSERT INTO person(name,surname,age,number,country) VALUES(?,?,?,?,?)''', dataAdd)
                persons.commit()
                choose()
                                

def choose():
    global option
    print('*' * 50)
    print('Welcome to the project area.')
                
    print('Which Project do you prefer.')  
    print(''' 1 - The multiplication table.
                        2 - Finding the largest and smallest number.
                        3 - Factor Calculation.
                        4 - Calculating the areas of geometric shapes.
                        5 - Reading file.
                        6 - File operations with os module.
                        7 - Find a prime number.
                        8 - Learning computer knowledge.
                        9 - Print the text backwards.
                        10 - Try Expect
                        11 - fibonacci Calculation - 1
                        12 - fibonacci Calculation - 2  
                        13 - Writing file.
                        14 - Exit''') 
                
    option = int(input('>>'))
                
    if option == 1:
        print('''   Difficulty Levels: 
            1 - Easy Mode
            2 - Normal Mode
            3 - Hard Mode
            4 - So Hard Mode ''') 
        option2  = int(input('>>>')) 

        if option2 == 1: 
            print(''' Easy Mode. ''')
            theMultiplication(1,10 + 1)  
            #choose()
                         
        elif option2 == 2:
            print(''' Normal Mode. ''')
            theMultiplication(10,20 + 1) 
            #choose()

        elif option2 == 3:
            print(''' Hard Mode. ''') 
            theMultiplication(20,30 + 1) 
            #choose()
 
        elif option == 4:
            print(''' So Hard Mode. ''')
            theMultiplication(30,40 + 1) 
            #choose()
        else:
            print('Out of Selection')  
            choose()
                    
                
    elif option == 2:
        bigSmall()
        choose()

    elif option == 3:
        factorCalculation()
        print('(Factor calculation with recursion). \n Which number of factorial would you like to take?  Sample(1,2,3,4,5,6,7)') 
        value = int(input('Value : ? >'))  
        print('Factor :',factorCalculation2(value)) 
        choose()

    elif option == 4:
        areaCalculation()
        choose()

    elif option == 5: 
        fileRead()
        choose()

    elif option == 6:
        print('''
        File operations with module 'os'
                -----------------------------
                1 - Creating a new folder
                2 - List the folders in the directory
                3 - Delete folder
        ''')
        try:
            fileOption = int(input('The transaction number you want to make ? :'))
            if fileOption == 1:
                newFolderCreate() 
                choose()
            if fileOption == 2:
                listDirectory()
                choose()
            if fileOption == 3:
                deleteFolder()
                choose() 
        except:
            print('Error.')
                
    elif option == 7:
        primeNumber()
        choose() 
                
    elif option == 8:
        computerInformation()
        choose() 

                
    elif option == 9:
        print('Reversing') 
        eversingOption = input('Which one would you like to do with ? ( 1 - Just Print , 2 - For, 3 - While' + ' :') 
        if eversingOption == 1:
            writeBackwardsprint() 
            choose()
            
        elif eversingOption == 2:
            writeBackwardsfor()
            choose()

        elif eversingOption == 3:
            writeBackwardwhile()
            choose()
        else:
            choose()
                
                
    elif option == 10:
        tryExpect() 
        choose()
                
    elif option == 11:
        fibonacciNumberValue = int(input('Fibonacci Enter Number : >>')) 
        print('Fibonacci Number Result :',fibonacciNumber(fibonacciNumberValue))  
        choose()
                
    elif option == 12:
        fibonacciNumber2() 
        choose()

    if option == 13:
        fileWrite()
        choose()
    
    if option == 14:
        exit()

def theMultiplication(startValue,FinishValue): 
    totalPoint = 0
    for i in range(startValue,FinishValue):
        for j in range(startValue,FinishValue):
            print('{} {} {} {} : ?'.format(i,'*',j,'?'))
            sonuc = int(input('Result : >>>'))
            if sonuc == int(i * j):
                print('{}'.format('True.'))
                totalPoint+=5
            else:
                print('{}'.format('Wrong Answer.')) 
                totalPoint+=-5 
                print('Total Point : ', totalPoint)

                choose()
                


def bigSmall():
    numberlist = []
    print('Finding the Big and Small Number.')
    piece = int(input('How many numbers will you enter ? :'))
    for f in range(1,piece + 1):
        num = int(input('Enter Number :'))
        numberlist.append(num) 
    print('Largest list number : {} and Smallest list number : {}'.format(max(numberlist),min(numberlist)))   
    

def factorCalculation():
    factor = 1
    print('Which number of factorial would you like to take?  Sample(1,2,3,4,5,6,7)') 
    value = int(input('Value : ? >'))  
    for a in range(1, value + 1):
        factor*=a
    print('Factorial of the number of {} ​​you entered : {}'.format(value,factor)) 


def factorCalculation2(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorCalculation2(n - 1) 
                

def areaCalculation():
    print("{}".format('Calculating the areas of geometric shapes.'))  
    print("{}".format('Which shape would you like to calculate the area ? :'))
    print('''
    \n Square : 1
    Rectangle : 2
    Trapezoid : 3
    Parallelogram : 4
    Equilateral Quadrangle : 5
    ''')
    value = int(input('Which Figure ? :'))
            
    if value == 1:
        r = int(input('Enter Radius :'))   
        print('Area of ​​the Square: {}'.format(r**2)) 
        return
            
    elif value == 2:
        short = int(input('Enter a short edge :'))
        tall = int(input('Enter a tall edge :')) 
        print('Area of ​​the Rectangle: {}'.format(short * tall)) 
        return
            
    elif value == 3:
        base = int(input('Enter a base :')) 
        base2 = int(input('Enter a base :'))
        height = int(input('Enter a height :'))
        print('Area of ​​the Trapezoid: {}'.format((base + base2) * height) / 2)   
        return
            
    elif value == 4:
        basee = int(input('Enter a base :'))
        heightt = int(input('Enter a height :'))
        print('Area of ​​the Parallelogram: {}'.format(basee * heightt))  
        return
            
    elif value == 5:
        side = int(input('Enter a side :'))
        heighttt = int(input('Enter a tall edge :'))
        print('Area of ​​the Equilateral Quadrangle: {}'.format(side * heighttt))  
        return


def fileWrite():
    while True:
        fileName = input('Enter Filename : ')
        if fileName == '':
            print('Do not leave the fields blank.')
        else:
            break

    with open('{0}.txt'.format(fileName),'a+') as fileName_:
        content = input('Content to Write in the File (If you want to write them separately, put a comma between them. Put an extra comma at the end) : ')
        fileName_.write(content)


def fileRead():
    while True:
        fileName = input('Enter Filename : ')
        if fileName == '':
            print('Do not leave the fields blank.')
        else:
            break

    if os.path.isfile('{0}.txt'.format(fileName)):
        with open('{0}.txt'.format(fileName),'r') as reading: 
            readingList = reading.readlines()
            for data in readingList:
                splitData = data.split(',')
                for data_ in splitData:
                    print(data_)
    else:
        print('There is no such file in the system.')


def newFolderCreate():
    folder = input('The name of the folder you will create: ')
    if os.path.exists(folder):
        print('{} There is already a folder named. Choose another name. '.format(folder))
    else:
        os.makedirs(folder)


def listDirectory():
    print('{}/\n...'.format(os.getcwd()))
    
    for z,d in enumerate(os.listdir(os.curdir)):
        print('{}  {}'.format(z, d))


def deleteFolder():
    directory = {}
    print('\nno\t\tfolder name\n--\t\t---------') 

    for ü,i in enumerate(os.listdir(os.curdir)):
        print("{}\t\t{}".format(ü, i))
        directory[ü] = i 

    try:
        d_no = int(input('The file number you want to delete : '))
        path = directory [d_no]
        os.removedirs(path)

    except Exception as except_:
        print('Error :', except_)



def primeNumber():
    num = int(input('Enter a Number :'))
    f = 0
    for g in range(2, num):
        if num % g == 0:
            f+=1
            print('Number Not Prime.')
            return

        if f == 0:
            print('Number Prime')




def computerInformation():
    print('\n OS : {}  \n Computer Name : {} \n Version : {}.'.format(os.platform,os.name,os.version))       


def  writeBackwardsprint():
    value = input('Type the text to be written in reverse : >>') 
    if value.isalpha():
        valeue = value[::-1]
        print('Before :{} After :{}'.format(value,valeue)) 

def writeBackwardsfor(): 
    t = ''
    value = input('Type the text to be written in reverse : >>') 
    if value.isalpha():
        for j in range(len(value)-1,-1,-1):
            t += value[j] 
            print('Before :{} After :{}'.format(value,t)) 

def writeBackwardwhile():
    t = ''
    num = 0
    value = input('Type the text to be written in reverse : >>') 
    lenn = len(value)
    if value.isalpha(): 
        while lenn > num:
            t+=value[lenn - 1] 
            num+=1


def tryExpect():
    nullList = []
    try:
        value = int(input('How many times will you enter a name ? >> ') ) 
        for t in range(0,value + 1):
            _value = input('Enter : ')
            nullList.append(_value) 
        for value in nullList:
            if value.endswith('ck'):
                value+='er'
                print('New Word :',value) 
            
    except Exception as except_:
        print('Error :', except_)
                

def fibonacciNumber(fibonacciNumberValue):
    if fibonacciNumberValue == 0:
        return 0
    elif fibonacciNumberValue == 1:
        return 1
    else:
        return fibonacciNumber(fibonacciNumberValue-1) + fibonacciNumber(fibonacciNumberValue-2)  


def fibonacciNumber2():
    value = []
    number1 = 1
    number2 = 1
            
    getNumber = int(input('Which number would you like to do the Fibonacci Calculation ? : '))  
    counter = 1
    
    while counter < getNumber:
        print(number1)
        value.append(number1)
        print(number2)
        value.append(number2)

        number1+=number2
        number2+=number1 
        counter+=2

    print('Value :',value) 


def areYouRegistered():
    name = ""
    yesORno = input('Are you registered : ')
    if yesORno == '':
        print('Do not leave the fields blank.')    
    if yesORno.upper() == 'Y':
        while True:
            name = input('Again Enter Name Please :') 
            if name == '':
                print('Do not leave the fields blank.')
            else:
                break
        
        with sqlite3.connect('persons.db') as persons:
            personsCursor = persons.cursor()
            personsCursor.execute('''SELECT * FROM person''')
            data = personsCursor.fetchall()

            for data_ in data:
                if data_[1].upper() == name.upper():
                    choose()
            
            exit()

    elif yesORno.upper() == 'N':
        getInformations()
        inforationSave()

areYouRegistered()
 






