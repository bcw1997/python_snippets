def intersection(a,b):
    index_one = 0
    index_two = 0

    result_array = []

    while index_one < len(a) and index_two < len(b):
        if(a)[index_one] == b[index_two]:
            result_array.append(a[index_one])
            index_one += 1
            index_two += 1
        
        elif a[index_one] > b[index_two]:
            index_two += 1
        
        else:
            index_one += 1

    print("The Intersection of the Arrays: \t")
    print(result_array)

intersection([1,3,5,7,9,11],[1,2,3,4,5,6])