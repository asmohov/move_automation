from patrol_calculator import patrol_sweep

#Begin user interface code
def patrol_frontend():
#Initialise return order booleans
    ret = 'n'
    cont= 'y'
    opt_route = 'y'
    party_size = 20
    ishostle = 'n'
    avd_list = ''
    print('Patrol Calculater, v2.0 Thermopylae')
    while cont == 'y':
        #reset inputs
        strt = ''
        spd = 0
        end = ''
        sdttm = 'now'
        avd_list = []
        #collect user inputs
        spd = float(input('Enter movement speed of the party '))
        prty_size = float(input('Enter size of party '))
        ishostle = input('Party is hostile? y/n ')
        print('When inputting remove apostrophes and spaces.')
        print('I.E. Wayfarer\'s Rest becomes WayfarersRest')
        strt = str(input('Enter starting province '))
        end = str(input('Enter ending province '))
        opt_route = str(input('Use optimal Route? y/n '))
        if opt_route != 'y':
            avd_list = str(input('Input provinces to avoid as a comma separated list '))
            avd_list.split(',')
        time = str(input('Enter time in DD/MM/YY HH:MM:SS format or enter \'now\' to use current time '))
        
        print('------------------------------------------------------------------')
        patrol_sweep(spd,strt,end,time,avd_lst=avd_list,party_size=prty_size,ishostile=ishostle)
        print('------------------------------------------------------------------')
        cont = str(input('Calculate another patrol sweep? y/n '))
    print('Exiting Program')
    
if __name__ == '__main__':
    patrol_frontend()