
def selection_sort(li):

    for r in range(len(li)):
        min_ind = r
        for i in range(r+1,len(li)):
            if li[min_ind]>li[i]:
                # print(li[min_ind],'>',li[i])
                min_ind = i
     
        li[r],li[min_ind] = li[min_ind],li[r]
        # print(li)
    
    print(li)

selection_sort([2,5,1,6,67])