#Front end UI code for land movement calculator, version 0.1 "Athina"

#path optimization method (DO NOT TOUCH)
import dijkstra_methods as dm
from datetime import datetime
from datetime import timedelta
import time

def movement(speed,start,end,sdatetime="now"):
    #give move speed as if a fast day 
    #default to current time
    if sdatetime == 'now':
        sdatetime=datetime.now()
    #time formatted as 'MM/DD/YYYY HH:MM:SS'
    #hardcode map in
    graph = dm.Graph('stormlands_node_map.txt')
    path,distance = graph.shortest_path(start,end)
    #calculate time based on whether you start in fast or slow day
    delta=12*distance/speed
    print('Total hours of travel is ',delta)
    end_time = sdatetime+timedelta(hours=delta)
    print('end time is: ',str(end_time))
    print(path)
    return path,end_time

#Begin user interface code
def main():
#Initialise return order booleans
    ret = 'n'
    cont= 'y'
    print('Land Movement Calculater, v0.1 Athina')
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
        time = str(input('Enter time in MM/DD/YY HH:MM:SS format or enter \'now\' to use current time '))
        print('------------------------------------------------------------------')
        p,e = movement(spd,strt,end,time)
        print('------------------------------------------------------------------')
        cont = str(input('Calculate another move order? y/n '))
    print('Exiting Program')
    
if __name__ == '__main__':
    main()
    
