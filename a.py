
def partition(li,low,high):
    pivot = li[low]
    i=low
    j=high-1

    while i<j:

        while pivot >= li[i] and i <=high:
            i+=1

        while pivot <= li[j] and j>=low:
            j-=1

        if i<j:
            li[j],li[i] = li[i],li[j]

    # li[low] = li[j]
    # li[j]=pivot
    # print(low)
    return li

li=[4,3,2,5,7,1]
print(partition(li,0,len(li)))