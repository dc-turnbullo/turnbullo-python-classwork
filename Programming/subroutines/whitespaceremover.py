import time

def oli_func(inp):
    arr = inp.split(" ")
    finalstr = ""
    for i in range(0, len(arr)):
        finalstr = finalstr + arr[i]

def jas_func(inp):
    inp.replace(" ", "")

uinupt = str(input("enter text"))
starttime = time.perf_counter_ns()
for _ in range(1000000):
    oli_func(uinupt)
endtime = time.perf_counter_ns()
completiontime = (endtime-starttime)/1000000
print(completiontime)