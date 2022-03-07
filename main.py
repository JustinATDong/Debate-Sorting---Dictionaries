# -*- coding: utf-8 -*-
"""

Justin Dong
CPSC 223P-01
Wed Feb 28, 2022
donganhtuanjustin@fullerton.edu

"""

# Maybe you can use some functions from the string module
import string

# This is the function that you must write the code for
def numWordsSpoken(candidate, word):
    """"This is a doc string that describes the function. Change it to your liking.
    Something like: This function returns the number of times a given word was 
    spoken by a given speaker"""

    # When a function is empty, this line is required to avoid a syntax error
    # When you add code here, remove "pass"
    pass


# This code will extract the data from the debate file and read it into one big
# string named debateString
debateFile = open("debate.txt", "r")
debateString = debateFile.read() 
debateFile.close()

# This code will extract the data from the stop words file and read it into one big
# string named stopWordsString
stopWordsFile = open("stopWords.txt", "r")
stopWordsString = stopWordsFile.read()
stopWordsFile.close()


# Start your code here
#Converting the strings to a list
NonoWords = stopWordsString.split()
YesyesWords = debateString.split()
 
#Variable Declaration
speakerText = "" #Empty list for the speaker's texts
obamaText = ["PRESIDENT", "BARACK", "OBAMA:"]
romneyText = ["MR.", "ROMNEY:"]
lehrerText = ["MR.", "LEHRER:"]

#New Empty dictionaries
obamaWords = {}
romneyWords = {}

#New variable for the cleaned up words
editedWord = ''

#Checking who is speaking
for words in YesyesWords:
    if words in obamaText:
        speakerText = "Obama"
        continue #ends current loop
    elif words in romneyText:
        speakerText = "Romney"
        continue
    elif words in lehrerText:
        speakerText = "Lehrer"
        continue

#Clean up the words within the debate.txt file and send it into the empty dictionaries, ignoring Lehrer
    match(speakerText):
        case "Obama":
            editedWord = words.lower().translate(str.maketrans('', '', string.punctuation))
            if (editedWord not in NonoWords) and (editedWord != ''):
                if editedWord not in obamaWords:
                    obamaWords[editedWord] = 0
                obamaWords [editedWord] += 1
        case "Romney":
            editedWord = words.lower().translate(str.maketrans('', '', string.punctuation))
            if (editedWord not in NonoWords) and (editedWord != ''):
                if editedWord not in romneyWords:
                    romneyWords[editedWord] = 0
                romneyWords [editedWord] += 1
        case "Lehrer":
            continue

#Sorting the lists
obamaTuple = [(v, k) for k, v in obamaWords.items()]
romneyTuple = [(v, k) for k, v in romneyWords.items()]

#Sorting the tuples and reversing to get the highest number of used words first
sortedObama = sorted(obamaTuple, reverse = True)
sortedRomney = sorted(romneyTuple, reverse = True)

#Printing out the top 40 words used
print("Obama")
for i in range(40):
    print(sortedObama[i][0], ':', sortedObama[i][1], end = " ")
print('\n')

print("Romney")
for i in range(40):
    print(sortedRomney[i][0], ':', sortedRomney[i][1], end = " ")






























