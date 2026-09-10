


# li=[8,4,2,5,7,1,10,3,11]
li=[-3,-9,0,-5]

largest=li[0]
for i in range(len(li)):
    if largest < li[i]:
        largest = li[i]

print(largest)

