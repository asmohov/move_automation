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

#helping method to determine if a patrol is hit
def isin(pattern, seq):
    for i in range(len(seq) - len(pattern) + 1):
        if seq[i:i+len(pattern)] == pattern:
            return True
    return False
#helping method for determining if a province has a holdfast
def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


def patrol_sweep(speed,start,end,sdatetime='now'):
    #initialise possible patrol list
    patrol_list = []
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
    path,time,dlta = movement(speed,start,end)
    print('checking for patrols--------------------------------------------------------')
    for patrol in patrol_list:
        desc = patrol[2]
        coordinates = patrol[0:2]
        #cut one tile patrols to the appropriate length
        if coordinates[1]=='0':
            coordinates=[coordinates[0]]
        #catch forward patrols
        if isin(coordinates,list(path)): 
            #calculate time delta and end time for a tripped patrol
            pth,endtime,dlta = clean_movement(speed,start,str(coordinates[-1]),sdatetime)
            print('patrol tripped at ',coordinates,' after ',str(dlta),' hours, at ',endtime.isoformat(sep = ' ',timespec='minutes'))
            print(desc)
        #catch reverse patrols
        elif isin(coordinates[::-1],list(path)):
            #calculate time delta and end time for a tripped patrol
            pth,endtime,dlta = clean_movement(speed,start,str(coordinates[-1]),sdatetime)
            print('patrol tripped at ',coordinates,' after ',str(dlta),' hours, at ',endtime.isoformat(sep = ' ',timespec='minutes'))
            print(desc)
    #holdfast detections
    for province in list(path):
        if not has_numbers(province):
            desc= 'Holdfast detection at '+province
            pth,endtime,dlta = clean_movement(speed,start,province,sdatetime)
            print('Holdfast detection at ',province,' after ',str(dlta),' hours, at ',endtime.isoformat(sep = ' ',timespec='minutes'))