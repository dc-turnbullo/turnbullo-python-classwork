deck = input().split(" ")
count = 0
final = ""
indexer = 0
while count < 13:
    final = final + deck[indexer]
    final = final + " "
    indexer += 4
    count += 1

print(final)
