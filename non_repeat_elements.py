"""
Take a string and return character that never repeats. 
If multiple uniques then return only the first unique

Very applicable to data security protocols. 
Also Linear TIme Solution
"""

def non_repeating(s):
    s = s.replace(" ", "").lower() # replace spaces, bring to lower case. 
    # Create Dictionary to track Key Value pair
    
    char_count = {}
    
    for c in s: 
        if c in char_count:
            char_count[c] += 1 # add +1 for particular c value
        else: 
            char_count[c] = 1 # give first occurence for particular c value 
        
        
    uniques = []
    item_sorter = sorted(char_count.items(), 
                         key = lambda x: x[1])
    
    for item in item_sorter: 
        if item[1] == item_sorter[0][1]:
            uniques.append(item) 
    
    return uniques

print(non_repeating('I Apple Ape Peels'))