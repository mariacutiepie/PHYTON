
def descOrder(li):
    li.sort()
    li.reverse()
    print (li)


#EX1
tu = (10,20,30,40,50)
li = list(tu)
print(descOrder(li))
print(li)
print(li.count(50))

#EX2
tu = (10,20,30,40)
a = tu[0]
b = tu[1]
c = tu[2]
d = tu[3]
print (a,b,c,d)

#EX3
tu = (11,22,33,44,55,66)
tucopy = tu[1:5]
print(tucopy)
fi = (77,88,99)
print(tucopy + fi)

#EX4
tu = ("orange", [10,20,30], (5,15,25))
# tu[0] = "banana"
print(tu[0])
a = tu[0]
print(a)




