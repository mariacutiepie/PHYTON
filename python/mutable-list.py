# li = [1,2,3,4,5,6,7,8,9,8]
# print (li)

# li[1] = 10

# print (li[1])

# # APPEND sa dulo magdagdag (takes a singeleton as a argument)
# li.append('a') 
# print(li)

# # INSERT is anywhere you want (takes a list as an argument)
# li.insert(2,'i')
# print(li)

# #EXTEND METHOD creates a fresh start list
# li.extend([10,11,12])
# print(li)
# print(li[8])

# li.append([10,11,12])
# print(li)
# print(li[9])

fi = [1,2,3,4,5,6,7,8,3,6,3]
#INDEX
# fi.index('a')

# #count
# fi.count('a')
# #remove
# fi.remove('a')
# print(fi)

fi = [1,2,3,4,5,6,7,8,3,6,3]
counter = fi.count(3)

print(counter)

for x in range(counter):
    fi.remove(3)
print(fi)

#REVERSE
fi.reverse()
print(fi)

fi = [1,2,3,4,5,6,7,8,3,6,3]

fi = list(tu)
tu = tuple(tu)
#SORT
# def descOrder()
# fi.sort()
# fi.reverse()
# print(fi)

# ci = [1,2,3,4,5,6,7,8,3,6,3]
# descOrder(ci)
# print(ci)