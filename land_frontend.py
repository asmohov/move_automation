#Front end UI code for land movement calculator, version 0.1 "Athina"

#path optimization method (DO NOT TOUCH)
import dijkstra_methods as dm
from datetime import datetime
from datetime import timedelta
import time


def movement(speed,start,end,sdatetime="now",avoid_list = []):
    #use main node map
    nodemap = 'main_nodemap.txt'
    #read time
    if sdatetime == 'now':
        sdatetime=datetime.now()
    elif isinstance(sdatetime,datetime):
        pass
    else:
        sdatetime = datetime.strptime(sdatetime,'%d/%m/%y %H:%M:%S')
    #time formatted as 'MM/DD/YYYY HH:MM:SS'
    #hardcode map in
    graph = dm.Graph(nodemap,avoid_list=avoid_list)
    path,distance = graph.shortest_path(start,end)
    #calculate time based on whether you start in fast or slow day
    delta=48*distance/speed
    print('Total hours of travel is ',delta)
    end_time = sdatetime+timedelta(hours=delta)
    print('end time is: ',str(end_time.isoformat(sep=' ',timespec='minutes')))
    print(list(path))
    return path,end_time,delta


def clean_movement(speed,start,end,sdatetime="now",avoid_list = []):
    nodemap = 'main_nodemap.txt'
    #movement with no print statements
    #read time
    if sdatetime == 'now':
        sdatetime=datetime.now()
    elif isinstance(sdatetime,datetime):
        pass
    else:
        sdatetime = datetime.strptime(sdatetime,'%d/%m/%y %H:%M:%S')
    #time formatted as 'MM/DD/YYYY HH:MM:SS'
    #hardcode map in
    graph = dm.Graph(nodemap,avoid_list=avoid_list)
    path,distance = graph.shortest_path(start,end)
    #calculate time based on whether you start in fast or slow day
    delta=48*distance/speed
    end_time = sdatetime+timedelta(hours=delta)
    return path,end_time,delta

#Begin user interface code
def land_frontend():
#Initialise return order booleans
    ret = 'n'
    cont= 'y'
    opt_route = 'y'
    avoid_list = []
    print('Land Movement Calculater, v1.2 Knossos')
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
        opt_route = str(input('Use optimal Route? y/n'))
        if opt_route != 'y':
            avoid_list = str(input('Input provinces to avoid as a comma separated list'))
            avoid_list.split(',')
        time = str(input('Enter time in DD/MM/YY HH:MM:SS format or enter \'now\' to use current time '))
        print('------------------------------------------------------------------')
        p,e,dlta = movement(spd,strt,end,time,avoid_list)
        print('------------------------------------------------------------------')
        cont = str(input('Calculate another move order? y/n '))
    print('Exiting Program')
    
if __name__ == '__main__':
    land_frontend()
    
