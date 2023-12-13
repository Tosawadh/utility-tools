import statistics as st

ver = '1.1.0'
print("Welcome to Utility Tools v" + ver,"\nType 'help' to display command list")
def help():
    print('Displaying command list')
    print('- help: Displays this menu')
    print('- id: ID digit 13 calculator')
    print('- stdev: Standard deviation calculator')
    print('- exit: Exit Utility Tools')
    return

def again():
    a = input('Make another input?(y/n): ')
    if a =='y':
        pass
    elif a =='n':
        menu()
    else:
        again()

def id():
    x = input('Enter your first 12 digit of your ID: ')
    n = ((13*int(x[0]))+(12*int(x[1]))+(11*int(x[2]))+(10*int(x[3]))+(9*int(x[4]))+(8*int(x[5]))+(7*int(x[6]))+(6*int(x[7]))+(5*int(x[8]))+(4*int(x[9]))+(3*int(x[10]))+(2*int(x[11])))%11      
    if len(x) != 12:
        print('Incorrect input')
        id()
    elif n <= 1:
        n = 1 - n
        print('Your 13th digit is:', n)
        print('Your ID number is', str(x)+str(n))
    elif n > 1:
        n = 11 - n
        print('Your 13th digit is:', n)
        print('Your ID number is', str(x)+str(n))
    else:
        print('Incorrect input')
        id()
    again()
    id()

def sd():
    x = []
    ps = str(input('[p]opulation or [s]ample size?: '))
    if ps == 'p':
        try:
            n = int(input('Enter population size: '))
            for i in range(0, n):
                num = float(input('Enter number: '))
                x.append(num)
        except:
            print('Incorrect type or no value has been inserted, aborting operation')
            menu()
        print('Calculation successful, displaying results...')
        print('Mean:', st.mean(x))
        print('Standard Deviation:', st.pstdev(x))
    elif ps == 's':
        try:
            n = int(input('Enter sample size: '))
            for i in range(0, n):
                num = float(input('Enter number: '))
                x.append(num)
        except:
            print('Incorrect type or no value has been inserted, aborting operation')
            menu()
        print('Calculation successful, displaying results...')
        print('Mean:', st.mean(x))
        print('Standard Deviation:', st.stdev(x))
    else:
        print('Enter a valid option')
        sd()
    again()
    sd()

def menu():
    util = input('util> ')
    if util == 'help':
        help()
        menu()
    elif util == 'id':
        print('Initilizing ID digit 13 calculator...')
        id()
        menu()
    elif util == 'stdev':
        print('Initilizing standard deviation calculator...')
        sd()
        menu()
    elif util == 'exit':
        print('Goodbye, user. Thank you for using Utility Tools')
        raise SystemExit
    else:
        print("Command '" + util + "' not available.")
        menu()

menu()