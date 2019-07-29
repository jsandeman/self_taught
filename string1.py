#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 04:50:15 2019

@author: jsandeman

String-manipulation exercises got The Self-Taught Programmer course
"""

### Excercise 1: print each character in the string "Camus"
###
for letter in "Camus":
    print(letter)

### Exercise 2: Input 2 strings and insert them into the tenplate:
### "Yesterday I wrote a [response_one]. I sent it to [response_two].
###
what_written = input("What did you write? ")
to_whom = input("To whom did you send it? ")
print(f"Yesterday I wrote a {what_written}. I sent it to {to_whom}!")

### Exercise 3: Captialize the first letter in the string
### "aldous Huxley was born in 1894."
###
### The capitalize() method will capitalize the 'A' in Aldous, but will
### convert everything else to lower case, so we'll split the process up
### to prevent that.
###
sentence = "aldous Huxley was born in 1894."
words  = sentence.split(' ')
words[0] = words[0].capitalize()
separator = ' '
new_sentence = separator.join(words)
print(new_sentence)

### Exercise 4: Split the sentence "Where now? Who now? When now?" into:
###    "Where now?", "Who now?", "When now?". The built-in split()
###    almost does the trick, but strips the delimiter string so the '?'
###    characters need to be added back.
sentence = "Where now? Who now? When now?"
sep_sentences = sentence.split('? ')
sep_sentences[0] += '?'
sep_sentences[1] += '?'
print(sep_sentences)

### Exercise 4: Replace every instance of "s" in "A screaming comes across the sky." with a dollar sign.
###
sentence = "A screaming comes across the sky."
new_sentence = sentence.replace('s', '$')
print(new_sentence)

### Exercise 5: Use a method to find the first index of the character "m" in the string "Hemingway".
###
word = 'Hemingway'
index = word.find('m')
print(f'The index of the first occurrence of the character \'m\' is {index}')

### Exercise 7: Create the string "three three three" using concatenation, and then again using multiplication.
###
three = " ".join(["three", "three", "three"])
alt_three = "three " *3
print(three)
print(alt_three)

