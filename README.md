# Debate Sorting - Dictionaries

## TLDR
In this activity, I create 2 empty Dictionaries for President Obama and Senator Romney to track every word that is said, ignoring Jim Lehrer's text. I strip the words from punctuation and capitilization differences and send them to it's respective dictionaries based on who said what. Then I print out the top 40 words said by each candidate.
      ## BIGGER PICTURE: TAG CLOUDS

## Transcript
The transcript is in *debate.txt*. It has a particular format. Each time one of the candidates speaks, that line is marked, e.g ‘PRESIDENT OBAMA:’. Once encountered, all words are attributed to that speaker until another label occurs (sometimes it is a question from the moderator, MR. LEHRER, so you have to ignore those). Take a look at the file.  I will provide the code to read the contents of this file into one big string.

## Stopwords
Not all words are worth counting. ‘a’, ‘the’, ‘was’, etc. are just junk. A list of such words is provided as stopWords.txt. No word in the stop word list should be counted in the tag cloud. I will provide the code to read the contents of this file into one big string. Some problems arise because our program cannot tell the difference between ‘american’ and ‘americans’. This is called a "stemming" problem. There are ways to address this issue, but it is not required for this assignment. 

# Requirements
Using the contents of the debate file and the stop words, your code **shall** create two dictionaries. One dictionary will be for Senator Romney, and the other for President Obama.  The keys for each dictionary **shall** be the words spoken by that candidate, and the values **shall** be the number of times those words were used.  The dictionaries **shall** exclude all words that are in the stop words list.

Your code **shall** print to the screen the 40 most frequently used non-stopwords and their counts.  See the example output below for the exact formatting.

A function shell will be provided for you, _numWordsSpoken(candidate, word)_.  Your code **shall** provide a return value of the number of times the given word was spoken by the given candidate. Comments in the code will help you with what to do.

# Assignment Notes: 
There are a couple of problems here. Think about each one before you start to program. 
 
1. Parsing the debate string. You have to separate the lines according to who said them: Obama, Romney, etc. Use the transcript format described above to help you with this. Remember, once you see one of the speakers’ tags (‘MR ROMNEY:’) all lines/words belong to that speaker until you see another speaker’s tag.

2. Once you have the words separated, you must remove all stop words (using the provided stopWords string. You can do this while you are collecting the words as well.  Also, remember to remove punctuation from words, just because a word comes at the end of a sentence and has a period at the end of it doesn’t make it a different word. (Importing string and using string.punctuation is a useful way to specify punctuation.)

3. You must then count the word frequency in the candidate’s words. Use a dictionary, where the key is the word and the value is the count.

4. Once you have a dictionary for each candidate, you must extract the 40 most frequently used non-stopwords and their counts.   Since a dictionary is unordered you need to create (count,word) tuples, put them in a list, and then sort the list.  Put count first in the tuple because sorting (using either sort or sorted) will sort on the first item.

# Getting Started 
1. Do the normal startup stuff (download the Git repository and create a project on your hard drive) 
2. Write a high-level outline of what you want to do. Think before you code. 
3. Start by trying to parse the debate text into its three parts: Obama, Romney, everything else (junk). If it makes it easier you can extract a little bit of the file (copy/paste) and make a smaller string so you can see what’s going on with something more simple. Once done, try it out on the big string.
4. Try to do a count of one candidate’s words in a dictionary. Again, use a small string so you can look at the results.
5. Try to extract the top counts in a dictionary.
6. Take a list of words and counts (make some up to start with if you like) and test the function _numWordsSpoken()_.
