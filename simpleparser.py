#-------------------------------------------------------------------------------
# Assignment 1
# Question 2
# Simpleparser.py asks the user to input their ID number and then decodes that 
# number to print out their birthdate, gender and citizenship status
#-------------------------------------------------------------------------------
# Author: Claire Snibbe : SNBCLA001
# Date:   2 Mar 2019
#---------------------------- ---------------------------------------------------

cIdnumber = input('Please enter your ID number:\n')
#
#ideally I would have had validation on the length of the cIdnumber as being 13
#
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

#-------------------------------------------------------------------------------