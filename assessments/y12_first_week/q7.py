def twohigh(my_2d_array):
    i = 0
    highestj = 0
    highesti = 0
    highest = my_2d_array[0][0]  
    
    while i < len(my_2d_array):
        j = 0
        a = my_2d_array[i]
        while j < len(a):
            if a[j] > highest:  
                highesti = i
                highestj = j
                highest = a[j]
            j += 1  
        i += 1  
    
    print("The highest value is " + str(highest) + " in row " + str(highesti) + " column " + str(highestj))


my_2d_array = [[2, 5, 7], [5, 1, 6], [16, 3, 2]]


twohigh(my_2d_array)