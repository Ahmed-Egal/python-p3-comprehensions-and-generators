#!/usr/bin/env python3

def return_evens(num_list):
    return [n for n in num_list if n % 2 == 0]

def make_exclamation(sentence_list):
    return [(i + "!") for i in sentence_list]





#print(return_evens([0,1,3,5,7,8,9,10,12,14,15,17]))

print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))