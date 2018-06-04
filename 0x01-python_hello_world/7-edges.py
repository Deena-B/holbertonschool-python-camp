#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]       #keeps the first 3 letters of the variable word
word_last_2 = word[-2:]       #keeps the last 2 characters of word 
middle_word = word[1:-1]      #keeps all but 1st and last character of word
print("First 3 letters: {}".format(word_first_3))
print("Last 2 letters: {}".format(word_last_2))
print("Middle word: {}".format(middle_word))
