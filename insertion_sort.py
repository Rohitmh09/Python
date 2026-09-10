
def insertion_sort(li): # my way code as per understanding

    for i in range(1,len(li)):
        j=i-1
        key = li[i]
        while j>=0:
            if li[j] > key:
                li[j+1] = li[j]
                if j==0:
                    li[j] = key
            else:
                li[j+1] = key
                break
            j-=1
    
    print(li)

def insertion_sort_standards(li):

    for i in range(1,len(li)):
        j = i-1
        key = li[i]

        while j>=0 and li[j] > key:

            li[j+1] = li[j]
            j-=1
        li[j+1] = key
    print('Standard Sort: ',li)

insertion_sort([5,1,2]) #my way
insertion_sort_standards([5,1,2])
