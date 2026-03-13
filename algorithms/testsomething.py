input_str = "10 20 2 770 33 30 67 1 7 9"

arr = [int(x) for x in input_str.split()]


arr.sort()


output = " ".join(map(str, arr))

print(f"Sorted Array: {arr}")
print(f"Formatted String: {output}")
