import random
import string

def convert2poem(s):
    s = s.translate(str.maketrans('', '', string.punctuation)) #remove punctuations
    s = s.split() #splitting the string words into an array
    maxwords = 5 #maximum number of words each line can include
    ptr = 0 #initial word pointer
    nxtptr = random.randint(2,maxwords) #picking a random number of words to print

    while nxtptr <= len(s)+maxwords: #print till pointer is less than or equal to number of words. Had to add maxwords or else it wouldnt print the rest of the words 
        line  = s[ptr:nxtptr] #select words into a line
        ptr = nxtptr #make initial pointer to next one
        nxtptr += random.randint(2,maxwords) #go to the next random amount of words
        print(" ".join(line)) #join array of words separated by a space
        


with open('text.txt','r') as file:
    s = file.read()

convert2poem(s)