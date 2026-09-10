

def rev_list_fun(li,left_index,right_index):

    if right_index<=left_index:
        return

    # temp=li[right_index]
    # li[right_index]=li[left_index]
    # li[left_index]=temp

    li[left_index],li[right_index]=li[right_index],li[left_index] #It is work as swapping in python

    rev_list_fun(li,left_index+1,right_index-1) #Time Complexity = O(N/2) = O(N), Space Complexity=O(N)-->Stack Space


def rev_list_while(li,left,right):

    while left<=right:
        li[left], li[right] = li[right], li[left]
        left+=1
        right-=1
    return 


if __name__=="__main__":
    print('JAY SHREE RAM')
    li=[5,7,3,2,6,1,5]
    print('Original List:',li)
    # rev_list_fun(li,0,len(li)-1)
    rev_list_while(li,2,5)
    print('Updated List:',li)