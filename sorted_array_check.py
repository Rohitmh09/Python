
def check_array(arr):
    is_asc = True
    is_desc =True

    for r in range(len(arr)-1):
        if arr[r] > arr[r+1]:
            is_asc = False
        else:
            is_desc = False

        print('r:',arr[r],' r+1:',arr[r+1])


    if is_asc or is_desc:
        if is_asc:
            print('array sorted in ascending order')
        else:
            print('array sorted in desc order')
    else:
        print('not sorted array')


check_array([2,2,2])



