# Author: Brian Hoang
# Date: 11/20/2019
# Description: function that takes in string and returns a dictionary of letters as keys and number
# of times those letters appear in the string


#takes in mystring as parameter for count_letters
def count_letters(mystring):
    tally = 0
    #string to check for characters that aren't letters
    secstring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #creates dictionary for letters
    dic_letters = {}
    #makes all letters in string capitalized
    mystring = mystring.upper()
    #for loop to iterate through string to check for new or existing letters or non-letters
    for tally in range(len(mystring)):
        if mystring[tally] not in secstring:
            tally+=1
        elif mystring[tally] in dic_letters:
            #adds 1 if letter exists
            dic_letters[mystring[tally]] += 1
            tally +=1
        elif mystring[tally] not in dic_letters:
            #sets dictionary to 1 if letter has not been created
            dic_letters[mystring[tally]] = 1
            tally+=1

    return dic_letters


#string = "appl34esauce"
#print(count_letters(string))