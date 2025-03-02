#-------------------------------------------------------------------------------
# Assignment 1
# Question 4
# Tracking. logs information on endangered animals being tracked for a 
#conservation study. Prompts the user for animal identity codes and then responds
#to the following commands :
#print : print the last known location of each animal
#log : record that the animal with given identity code was last observed at the 
#<x,y> co-ordinate location
#quit: terminate the program
#-------------------------------------------------------------------------------
# Author: Claire Snibbe SNBCLA001
# Date: 8 March 2019
#-------------------------------------------------------------------------------
animals = dict()   # create dictionary of animals to store animal ids & location
codelist = []      # create list to store animal ids<
commandlist = []   # create list of valid commands
commandlist.append('print')
commandlist.append('log')
commandlist.append('quit')
#-------------------------------------------------------------------------------
# Enter the animal identity codes.

print("Please enter the animal identity codes.(Press return when done.)")
code1 = input('Animal no. 1:\n')
code2 = input('Animal no. 2:\n')
code3 = input('Animal no. 3:\n')
if code1 != '':
  codelist.append(code1)
if code2 != '':
  codelist.append(code2)
if code3 != '':
  codelist.append(code3)
print('Commands: print, log animal_id x_ord y_ord, quit.')
command = 'X'
while command != 'quit':
    command = input('Enter command:')
   
    if not command in commandlist and not command[0:3] in commandlist:    # e.g. Pront instead of Print
      print('Could not interpret command.')
      print('Commands: print,log, quit.')   
    
    if command == 'print':

# print the last known locations of each animal
#-------------------------------------------------------------------------------
      for codex in codelist:
          if (animals.get(codex)) == None:
            print ('Animal ' + codex + ' cannot be located.')
          else:  
            print('Animal ' + codex + ' last seen at ', end = "")
            print(str(animals[codex]).replace('[','(').replace(']',')')+".") 

    if command[0:3] == 'log':
      dictlist = command.split()
      animals.update({dictlist[1]:[int(dictlist[2]), int(dictlist[3])] })
      
 
       
































