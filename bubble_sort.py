
def sort_fun(li):

    size = len(li)
    for r in range(size-2,-1,-1): #Tc = O(n(n+1)/2) = O(n^2)
        is_swap = False
        for i in range(0,r+1):
            if li[i] > li[i+1]:
                li[i],li[i+1] = li[i+1],li[i]
                is_swap = True #IF its True then array is unsorted if single time it False means it is sorted

        if not is_swap:
            print('Already Sorted')
            break
    print(li)


if __name__=='__main__':
    print('JAY SHREE RAM')
    sort_fun([1,2,6,4,5])