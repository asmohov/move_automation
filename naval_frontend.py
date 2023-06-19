#Front end UI code for land movement calculator, version 0.1 "Athina"

#path optimization method (DO NOT TOUCH)
import dijkstra_methods as dm
from datetime import datetime
from datetime import timedelta
import time
from patrol_calculator import init_provinces

def nmovement(speed,start,end,sdatetime="now",avoid_list = []):
    #use main node map
    nodemap = 'navalnodemap.txt'
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


def nclean_movement(speed,start,end,sdatetime="now",avoid_list = []):
    nodemap = 'navalnodemap.txt'
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
def naval_frontend():
#Initialise return order booleans
    #dictionary of all provinces
    prov_dict=init_provinces()
    openwater = 'n'
    cont= 'y'
    opt_route = 'y'
    print('Naval Movement Calculater, v1.1 Syracuse')
    while cont == 'y':
        avoid_list = []
        openwater_list = []
        temp_list = []
        #reset inputs
        strt = ''
        spd = 0
        end = ''
        sdttm = 'now'
        #collect user inputs
        spd = (input('Enter movement speed of the party or \'lorecog\' :'))
        if spd == 'lorecog':
            spd =20
        else: spd = spd
        print('When inputting remove apostrophes and spaces.')
        print('I.E. Wayfarer\'s Rest becomes WayfarersRest')
        strt = str(input('Enter starting province '))
        end = str(input('Enter ending province '))
        openwater = str(input('Use Open Water? y/n '))
        if openwater == 'n':
            for i in range(1,60):
                i = 'OS'+str(i)
                openwater_list.append(i)
        avoid_list = avoid_list+openwater_list
        #avoid ports if they are not the end
        for key in prov_dict:
            if key != strt and key!=end and len(key)>3:
                avoid_list.append(key)
        #open water section
        opt_route = str(input('Use optimal Route? y/n '))
        if opt_route != 'y':
            temp_list = str(input('Input provinces to avoid as a comma separated list '))
            temp_list = temp_list.strip(' ')
            temp_list=temp_list.split(',')
        avoid_list = avoid_list+temp_list
        time = str(input('Enter time in DD/MM/YY HH:MM:SS format or enter \'now\' to use current time '))
        print('------------------------------------------------------------------')
        p,e,dlta = nmovement(spd,strt,end,time,avoid_list)
        openwater_number = 0
        for prov in list(p):
            if 'OS' in prov:
                openwater_number+=1
        print('Open Water provinces travelled: ',openwater_number)
        print('------------------------------------------------------------------')
        cont = str(input('Calculate another move order? y/n '))
    print('Exiting Program')
    
if __name__ == '__main__':
    naval_frontend()
    
