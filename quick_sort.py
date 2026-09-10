
def partition(li,low,high):
    pivot = li[low]
    i=low
    j=high

    while i<j:

        while pivot >= li[i] and i <high:
            i+=1

        while pivot <= li[j] and j>low:
            j-=1

        if i<j:
            li[j],li[i] = li[i],li[j]

    li[j],li[low] = li[low],li[j]
   
    return j



def quick_sort(li,low,high):

    if low<high:
        p_index = partition(li,low,high)
        # print('list:',li,' index:',p_index+1,' high:',high)

        quick_sort(li,low,p_index-1)
        # print('list:',li,' index:',p_index+1,' high:',high)
        quick_sort(li,p_index+1,high)



li=[8,4,2,5,7,1,10,3]
quick_sort(li,0,len(li)-1)
print(li) 