def Highestvalue(my_array):
    max = 0
    length = len(my_array)
    for i in range(0,length):
        if my_array[i] > max:
            max = my_array[i]
    
    print(max)

my_array = [8,1,-6,9,15,7,2,16]
Highestvalue(my_array)