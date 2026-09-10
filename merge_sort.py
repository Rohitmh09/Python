
def merge_sort(li):

    if len(li) <=1:
        return li
    
    mid = len(li)//2
    # print(mid)

    left_part = merge_sort(li[:mid])
    right_part = merge_sort(li[mid:])

    return merge(left_part,right_part)




def merge(left_part,right_part):
 l=0
 r=0
 arr=[]
#  print('left:',left_part,' right:',right_part)
 while l < len(left_part) and r < len(right_part):

    if left_part[l] < right_part[r]:
       arr.append(left_part[l])
       l+=1
    else:
       arr.append(right_part[r])
       r+=1

 while l < len(left_part):
    arr.append(left_part[l])
    l+=1
 while r < len(right_part):
    arr.append(right_part[r])
    r+=1
 print('left:',left_part,' right:',right_part, 'current output:',arr)

 return arr
 




print('final output:',merge_sort([2,3,1,5,6,4,1])) 

