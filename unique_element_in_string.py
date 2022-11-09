#Given a string are all the characters unique?

#Python Structures 

from cgitb import strong
from dataclasses import replace


def unique(string):
    string = string.replace(' ', '')
    return len(set(string)) == len(string)

print(unique('a b cdef'))

# Another way

def unique_1(s):
    s = s.replace(' ', '')
    characters = set()
    
    for letter in s: 
        if letter in characters:
            return False
        else: 
            characters.add(letter)
    return True
         
         
         
print(unique_1('acdzf'))
