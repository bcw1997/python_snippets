#What is the most frequently occuring element in that array? In O(n)

def most_frequent(list):
    count = {}
    max_count = 0
    max_item = None
    
    for i in list:
        if i not in count:
            count[i] = 1
        else: 
            count[i] += 1
            
        if count[i] > max_count:
            max_count = count[i]
            max_item = i
    return max_item


my_array = [1,1,1,1,1,1,3,4,4,4,5,5,5,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,8,9,10]
print(most_frequent(my_array))