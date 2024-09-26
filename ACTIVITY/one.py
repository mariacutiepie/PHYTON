tup = ('a', 'b', 'a', 'c', 'a', 'd', 'b')
mostElement = None
counter = 0

for element in tup:
    count = tup.count(element)
    if count > counter:
        counter = count
        mostElement = element

positions = []
for x in range(len(tup)):
    if tup[x] == mostElement:
        positions.append(x)


print(f"The most frequent element is '{mostElement}' and it appears {counter} times at positions {positions}.")
