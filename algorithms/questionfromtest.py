inputarr = [7,3,6,7,5,3,2,3,6]
checkingarr = [0 for i in range(0,len(inputarr))]
for i in range(0,len(inputarr)):
    checkingarr[inputarr[i]-1] +=1
for i in range(0,9):
    if checkingarr[i] !=0: 
        print(f"number {i+1} came up {checkingarr[i]} times")
