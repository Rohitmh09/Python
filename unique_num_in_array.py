

def check_duplicate():

    size = int(input())
    num= list(map(int,input().split()))
    if not num:
        return 0
    i=0

    for j in range(1,size):
        if num[i]<num[j]:
            i+=1
            num[i]=num[j]


    print("nums:",num)
    print(i+1)

check_duplicate()


