'''#How to reverse the String wihtout built-in functions==Program1
s='VenkatReddy'   #defining the string
sr=''             #Taking an empty variable
for r in s:       #For loop to perform reverse operations
    print(r)      #Printing what the r is taking
    sr=r+sr       #concating the sr valur to the r and assigning it to sr
print(sr)         #finally out of the loop printing the reversing of the String.'''

'''#How to chagne the particular letter in a string word?==Program2
s='This is rold'                #Degfining the String
spl=list(s)                     #converting String into List data type
print(spl)                      #Printing the list
print(spl.index('r'))           #finding the index of the character you want to change
spl[8]='g'                      #changing the character
print(spl)                      #Printing the list after changing
op=''.join(spl)                 #Converting list characters into a String
print(op)                       #Printing the final string output.'''

'''#How to count the number of char's and captillatters in a String==Program-3
s='Hello Venkat 143'            #Degfining the String
sc=''                           #Taking an empty variable for characters
sn=''                           #Taking an empty variable for digits
for i in s:                     #For loop to perform operations
    if i.isalpha():             #checking that is it alphabet or digit
        sc=sc+i                 #if it is alphabet concate to sc
        #print(Sc)
    else:
        sn=sn+i                 #if it is digit  concate to sn
    #print(sn)
print(sc+'\n'+sn)
print('Total number of characters are:',+len(sc)) #coutning the total number of alphabets
print('Total number of digits are:',+len(sn))     #coutning the total number of digits'''

#How to count the repeated words in a string ?==Program4
    
'''#How to convert string to list in python?==Program5
s='Venkat143'                   #Degfining the String
l=list(s)                       #built in list function 
print(l) '''
    
#How to convert string to dictionary in python ?==Program6

'''#How to convert string to tuple in python==Program7
s='hello venkey'                #Degfining the String
print tuple(s)                  #built in list function '''

'''#How to convert string to int ?==Program8
s='123'                         #Degfining the String
n=int(s)                      #Using the type convetion method int
print n'''

'''#How to convert string to float?==Program9
s='123.56'                         #Degfining the String
n=float(s)                      #Using the type convetion method int
print n'''

#How to convert stirng to number format ?==Program10

'''#How to split the int and string sapart?==Program11
s='Hello number 1 Venkat 143'            #Degfining the String
sc=''                           #Taking an empty variable for characters
sn=''                           #Taking an empty variable for digits
for i in s:                     #For loop to perform operations
    if i.isalpha():             #checking that is it alphabet or digit
        sc=sc+i                 #if it is alphabet concate to sc
        #print(Sc)
    elif i.isdigit():
        sn=sn+i                 #if it is digit  concate to sn
    #print(sn)
print sc
print sn  '''

#what is height value in a string using for python?==Program12

13) what is repeted world using for python ?====Program13

14)How to print the (a,e,i,o,u) in string?====Program14

15)How to print the order latters in strin ?==Program15

16)How to replace the string Program16

