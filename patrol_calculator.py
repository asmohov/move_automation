#patrol calculator
#to be included, patrols MUST be in the sample_patrols.txt file in the following format:
#IF patrol in only one province:
#Province/0/description
#IF on a bridge
#Province1/Province2/description
#order unimportant

from land_frontend import movement
from land_frontend import clean_movement
import dijkstra_methods as dk
from datetime import datetime
from datetime import timedelta
import time


    
#helping method to assign province ownership
def init_provinces():
    d = {}
    with open("province_catalog.txt") as f:
        for line in f:
            (key, val) = line.split('\t')
            val = val.strip('\n')
            d[(key)] = val
    return d

#helping method to determine if a patrol is hit
def isin(pattern, seq):
    for i in range(len(seq) - len(pattern) + 1):
        if seq[i:i+len(pattern)] == pattern:
            return True
    return False
#helping method for determining if a province has a holdfast
def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

#helping method to print out holdfast detections along a path
    for province in list(path):
        if not has_numbers(province):
            desc= 'Holdfast detection at '+province
            pth,endtime,dlta = clean_movement(speed,start,province,sdatetime,avd_lst)
            print('Holdfast detection at ',province,' after ',str(dlta),' hours, at ',endtime.isoformat(sep = ' ',timespec='minutes'))


def patrol_sweep(speed,start,end,sdatetime='now',avd_lst = [],party_size = 20,ishostile='n'):
    #initialise possible patrol list
    patrol_list = []
    #initialise province dictionary
    prov_dict = init_provinces()
    #read patrol database
    filename = './sample_patrols.txt'
    with open(filename) as fhandle:
        next(fhandle)
        for line in fhandle:
            #print(line)
            p1,p2,desc = line.split('*')
            patrol_list.append([p1,p2,desc])
    #print(patrol_list)
    #set datetime
    if sdatetime=='now':
        sdatetime = datetime.now()
    elif isinstance(sdatetime,datetime):
        pass
    else:
        sdatetime = datetime.strptime(sdatetime,'%d/%m/%y %H:%M:%S')
    path,time,dlta = movement(speed,start,end,sdatetime,avd_lst)
        #patrols and controlled passages ALWAYS cause detections

    print('checking for patrols--------------------------------------------------------------------------------')
    for patrol in patrol_list:
        desc = patrol[2]
        coordinates = patrol[0:2]
        #cut one tile patrols to the appropriate length
        if coordinates[1]=='0':
            coordinates=[coordinates[0]]
        #catch forward patrols
        if isin(coordinates,list(path)): 
            #calculate time delta and end time for a tripped patrol
            pth,endtime,dlta = clean_movement(speed,start,str(coordinates[-1]),sdatetime,avd_lst)
            print('patrol tripped at ',coordinates,' after ',str(dlta),' hours, at ',endtime.isoformat(sep = ' ',timespec='minutes'))
            print(desc)
        #catch reverse patrols
        elif isin(coordinates[::-1],list(path)):
            #calculate time delta and end time for a tripped patrol
            pth,endtime,dlta = clean_movement(speed,start,str(coordinates[-1]),sdatetime,avd_lst)
            print('patrol tripped at ',coordinates,' after ',str(dlta),' hours, at ',endtime.isoformat(sep = ' ',timespec='minutes'))
            print(desc)

     #Detection Logic
    if party_size > 249 and ishostile == 'y':
        #big and hostile
        for province in list(path):
            desc= 'Province detection at '+province+', owned by '+prov_dict[province]+'.'
            pth,endtime,dlta = clean_movement(speed,start,province,sdatetime,avd_lst)
            print('Holdfast detection at ',province,' after ',str(dlta),' hours, at ',endtime.isoformat(sep = ' ',timespec='minutes'),', owned by '+prov_dict[province]+'.')
    elif party_size > 25 and ishostile == 'y':
        #medium and hostile
        #detection at holdfasts
        for province in list(path):
            if not has_numbers(province):
                desc= 'Holdfast detection at '+province
                pth,endtime,dlta = clean_movement(speed,start,province,sdatetime,avd_lst)
                print('Holdfast detection at ',province,' after ',str(dlta),' hours, at ',endtime.isoformat(sep = ' ',timespec='minutes'),', owned by '+prov_dict[province]+'.')
    elif ishostile == 'y':
        #small and hostile
        pass
    elif party_size > 249 and ishostile == 'n':
        #big and placid
        #detected at every province
        for province in list(path):
            pth,endtime,dlta = clean_movement(speed,start,province,sdatetime,avd_lst)
            print('Province detection at ',province,' after ',str(dlta),' hours, at ',endtime.isoformat(sep = ' ',timespec='minutes'),', owned by '+prov_dict[province]+'.')
    elif party_size >25 and ishostile == 'n':
        #medium and placid
        #holdfast detections
        for province in list(path):
            if not has_numbers(province):
                desc= 'Holdfast detection at '+province+', owned by '+prov_dict[province]+'.'
                pth,endtime,dlta = clean_movement(speed,start,province,sdatetime,avd_lst)
                print('Holdfast detection at ',province,' after ',str(dlta),' hours, at ',endtime.isoformat(sep = ' ',timespec='minutes'),', owned by '+prov_dict[province]+'.')
                print('Only local forces may react.')
    elif ishostile == 'n':
        #small and placid
        pass