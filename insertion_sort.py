
def insertion_sort(li): # my way code as per understanding

   for r in range(1,len(li)):  # [5,2,4,1]
       j = r-1                 # [1,24,3,2]
       key = li[r]
       while j>=0:
           if li[j] > key:
               li[j+1] = li[j]
               if j==0:
                   li[j] = key
           else:
               li[j+1] = key
           j-=1
           print(li)
   print(f'our list:{li}')
          


def insertion_sort_standards(li):

    for i in range(1,len(li)):
        j = i-1
        key = li[i]

        while j>=0 and li[j] > key:

            li[j+1] = li[j]
            j-=1
        li[j+1] = key
    print('Standard Sort: ',li)

insertion_sort([1,24,3,2]) #my way
insertion_sort_standards([5,1,2])
