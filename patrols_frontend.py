from patrol_calculator import patrol_sweep

#Begin user interface code
def patrol_frontend():
#Initialise return order booleans
    ret = 'n'
    cont= 'y'
    print('Patrol Calculater, v1.1 Rhodos')
    while cont == 'y':
        #reset inputs
        strt = ''
        spd = 0
        end = ''
        sdttm = 'now'
        #collect user inputs
        spd = float(input('Enter movement speed of the party '))
        print('When inputting remove apostrophes and spaces.')
        print('I.E. Wayfarer\'s Rest becomes WayfarersRest')
        strt = str(input('Enter starting province '))
        end = str(input('Enter ending province '))
        time = str(input('Enter time in DD/MM/YY HH:MM:SS format or enter \'now\' to use current time '))
        print('------------------------------------------------------------------')
        patrol_sweep(spd,strt,end,time)
        print('------------------------------------------------------------------')
        cont = str(input('Calculate another patrol sweep? y/n '))
    print('Exiting Program')
    
if __name__ == '__main__':
    patrol_frontend()