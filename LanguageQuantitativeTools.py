import string
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud

# Welcome to my bundle of code. Input of any language can be described by it in a quantitative manner. 
# In your disposal I give you a fixed sheme of letter entropy and frequency, following letter occurence and most important, word cloud!
# The comments will guide you, unccomment one plot at the time, unless you like to have mess :) Have fun!

##################
### Input text ###
##################
data = open("textFile.txt", 'r')  ### Supply your text here "textFile.txt ###
book = (data.read())
words = book.split()
wordLenght = np.zeros(len(words))

for wordX in range(len(words)):
    wordLenght[wordX] = len(words[wordX])

letters = string.ascii_lowercase
numletters = len(letters)
letterCounts = np.zeros(numletters)
n = 0

for i in letters:
    letterCounts[n] = book.lower().count(i)
    n += 1

letterProbability = letterCounts / sum(letterCounts)

######################
### Letter Entropy ###
######################
# fig, subpl = plt.subplots(1, figsize=(15, 5))
# subpl.bar(range(numletters), letterCounts)
# subpl.set_xticks(range(numletters))
# subpl.set_xticklabels(letters)
# subpl.set_xlabel('Letter')
# subpl.set_ylabel('Count')
# entropy = -sum(letterProbability * np.log2(letterProbability))
# subpl.set_title('Entropy = {}'.format(entropy))
# plt.show()
######################

probmatrix = np.zeros((numletters, numletters))

for i in range(len(book)-1):
    firstLetter = book[i]
    followingLetter = book[i + 1]
    if firstLetter in letters and followingLetter in letters:
        probmatrix[letters.index(firstLetter), letters.index(followingLetter)] += 1

##############################
### Following Letters Plot ###
##############################
# fig, subpl = plt.subplots(1, figsize=(10, 10))
# subpl.imshow(probmatrix, vmax=1000)
# subpl.set_xlabel('Next letter')
# subpl.set_ylabel('Observed letter')
# subpl.set_xticks(range(numletters))
# subpl.set_yticks(range(numletters))
# subpl.set_xticklabels(letters)
# subpl.set_yticklabels(letters)
# plt.show()
##############################


#######################
### Word Cloud Plot ###
#######################
#wordcloud = WordCloud().generate(book)
#plt.imshow(wordcloud)
#plt.axis('off')
#plt.show()
#######################
