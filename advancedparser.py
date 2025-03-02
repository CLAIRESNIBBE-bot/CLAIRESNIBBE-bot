#-------------------------------------------------------------------------------
# Assignment 1
# Question 3
# Advancedparser.py asks the user to input their ID number and then decodes that 
# number to print out their birthdate, gender and citizenship status - further to
# validate the 13th (check) digit to determine if the ID number is correct, by
# applying the Luhn algorithm.
#-------------------------------------------------------------------------------
# Author: Claire Snibbe : SNBCLA001
# Date:   6 Mar 2019
#-------------------------------------------------------------------------------
cIdnumber = input('Please enter your ID number:\n')
#print(cIdnumber)
#print(cIdnumber[0:12])
newIdnumber = cIdnumber[0:12]
total = 0
value = 0
for i in range(0,12):
   currchar = newIdnumber[i]
   #print(currchar)
   currpos = i
   current = int(newIdnumber[i]) 
   #print(current)
   #print(currpos) 
                            
   if currpos%2 == 0 :      # is position of index even or odd?
                            # exclude alternate digits
      #value = (current*2)%9
      value = (current*2)
      total = total + value
      #print('divisible by 2 for ' + str(current))
      #print('total is ' + str(total))
   else:
      #print('alternate value for ' + str(current))
      total = total + current
      #print('total is ' + str(total))
      
#print(total)   
checkvalid = 10 - total%10
#print(checkvalid)
lastdigit = int(cIdnumber[-1])
#print(lastdigit)
if checkvalid == lastdigit:
   # should call simpleparser as a function so that if code changes in simpleparser
   # then it does not have to be changed here as well!
   print('Your date of birth is '+ cIdnumber[4:6]+'/'+cIdnumber[2:4]+'/'+ cIdnumber[0:2]+'.')
   if int(cIdnumber[6:10])< 5000:
      gender = 'female.'
   else:
      gender = 'male.'
   print('You are '+ gender)  
   if cIdnumber[-3] == '1':
      citizen = 'a permanent resident.'
   else:
      citizen = 'a South African citizen.'
   print('You are ' + citizen)   
   
   
   
else:     
   print('Invalid ID number.')



   
   
      
      
      

  
  

