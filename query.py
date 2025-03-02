# #-------------------------------------------------------------------------------
# MIT - OOP Assignment 2
# Question 3
# query.py aims to query a set of bus timetable, as triggered by various queries
# by a bus-user :
# help : view all possible queries
# 1. load <route number>
# 2. next <embark_point> <from_time>
# 3. arrival <embark_point> <embark_time> <destination>
# 4. departures <embark_point> <destination> <earliest_arrival> <latest_arrival>
# 5. quit
#-------------------------------------------------------------------------------
# Author: Claire Snibbe SNBCLA001
# Date :  7 April 2019
#-------------------------------------------------------------------------------

from datetime import time
import re
    
def timeConvert(string ):
    
    """ Converts a string which contains a date into a date  """
    
    string = string.strip()
    if string.find(':') == 1:
      hour = int(string[0:1])
    else:
      if string.find(':') == 2:
        hour = int(string[0:2])
    mins = int(string[-2:])    
    time1 = time(hour,mins)
    time2 = time1.strftime('%H:%M')
    return time2   
#-------------------------------------------------------------------------------    
def pophelplist(helplist):
    
    """ Populate helplist with available commands """
    
    helplist=['load <route number>', 'next <embark_point> <from_time>',
               'arrival <embark_point> <destination>',
               'departures <embark_point> <destination> <earliest_arrival><latest_arrival>']
    
    print('Available commands:')
    for i in range(len(helplist)):
      print(helplist[i])

#-------------------------------------------------------------------------------             
def loadroute(route,busroute):
    """ Reads in a bus route to dictionary busroute with the destination as key"""
    
    route= route.replace("load",'').strip()+'.txt'
    file_input = open(route, 'r') 
    entries = []
    for line in file_input:    
        entries.append(line)    
    for i in range(0,len(entries)):           
        currententry = entries[i]
        pos = currententry.find('%')
        dest = currententry[0:pos-1]
        #print(currententry, dest)
        listedentry = re.split(r"\,",currententry[pos+1:])
        for k in range(0,len(listedentry)):         
           listedentry[k] = listedentry[k].replace("\n",'')  
           listedentry[k] = listedentry[k].strip()
           listedentry[k] = timeConvert(listedentry[k])
        busroute.update({dest:listedentry})            
    #print(busroute)
#-------------------------------------------------------------------------------
def find_next_trip(busroute,destination, departtime,nextlist):
    destination = destination.strip()
    value = busroute.get(destination)
    #print(destination, departtime)
    #print(value)
    argtime = timeConvert(departtime)
    list1 = []
    for i in range(len(value)):      
      listitem = timeConvert(value[i])
      if listitem > argtime:          
         list1.append(listitem)     
   
   # below,find the position in the bus list of departure times, corresponding
   # to the next bus departing, as it will be needed as a pointer to the arrival
   # time at the next destination.  Store in list nextlist.
   
    if len(list1) > 0 : 
        nexttrip = min(list1)
        nextlist.append(nexttrip)
        nextslot = value.index(nexttrip)          
        #print(nextslot)
        nextlist.append(nextslot)
    else:
       nextlist.append("HH:MM")
       nextlist.append('N/A')
#-------------------------------------------------------------------------------       
   
def find_depart_and_arrive(busroute,destination,departtime,destinationnext,nextlist):
    """                                                           """
    find_next_trip(busroute,destination, departtime,nextlist)
    if nextlist:
       value = busroute.get(destinationnext)
       #print(value)
       #print(nextlist[1])
       matchindex = nextlist[1]
       matchtime = value[matchindex]
       #matchtime = value[nextlist[1]]
       #print(matchtime)
    return matchtime  
#-------------------------------------------------------------------------------    
def range_for_arrive_and_depart(busroute,destination,destinationnext,arrivetimefirst, arrivetimelast, departlist):
    """                                                                        """
    value_arrive = busroute.get(destinationnext)
    #print(value_arrive)     
    arrivelist = []
    arrivetimefirst = timeConvert(arrivetimefirst)
    arrivetimelast = timeConvert(arrivetimelast)
    for i in range(len(value_arrive)):
        time = timeConvert(value_arrive[i])
        if time >= arrivetimefirst and time <= arrivetimelast:
            timeslot = i
            arrivelist.append(i)
    #print(arrivelist)
    
    value_depart = busroute.get(destination)
    #print(value_depart)
    for i in range(len(value_depart)):
        for j in range(len(arrivelist)):
            if arrivelist[j] == i: 
               departlist.append(value_depart[i])
    #print(departlist)

     
    
    

#-------------------------------------------------------------------------------        
  
def main():
    busroute = dict()    
    helplist = []
    nextlist = []  
    userinput = input('>')
    while userinput != "quit":      
        
      inputlist = userinput.split()
      
      if inputlist[0] == 'help':
         pophelplist(helplist)
      if inputlist[0] == 'next': 
         if not busroute:
            print('You must load a route first.')
         else:
            timepos = userinput.find(':')           
            #destination = userinput[5:timepos-2]
            destination = inputlist[1]
            departure = inputlist[2]
            #departure = userinput[timepos-2:]
            nextlist = []
            find_next_trip(busroute,destination,departure,nextlist)
            next = nextlist[0]
            if next != "HH:MM":
                print('The next bus departing from '+ destination + ' is at ' + next)
            else:
                print('Sorry, no departures found')

      if inputlist[0] == 'load':
           print('Done')
           loadroute(userinput,busroute)
        
      if inputlist[0] == 'arrival':
            destination = inputlist[1]
            departtime = inputlist[2]
            destinationnext = inputlist[3]                        
            arrivetime=find_depart_and_arrive(busroute,destination,departtime,destinationnext,nextlist)
            print('The next bus departing from ' + destination + ' arrives at ' + destinationnext + ' at ' + arrivetime)
            
      if inputlist[0] == 'departures':
           destination = inputlist[1]
           destinationnext = inputlist[2]
           arrivetimefirst = inputlist[3]
           arrivetimelast = inputlist[4]
           departlist = []
           range_for_arrive_and_depart(busroute,destination,destinationnext,arrivetimefirst, arrivetimelast, departlist)
           timestring = ''
           for time in departlist:
             timestring += time + ', '
           timestring = timestring[0:len(timestring)-1]
           print('Buses arriving at ' + destinationnext + ' in that period depart from ' + destination + ' at ' +
           timestring)
        
    
      userinput = input('>')   
    
    
    
    
if __name__ == "__main__":
    main()
    