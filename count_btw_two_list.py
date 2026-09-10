


def find_count_in_list(normal_list,map_list):

    for r in range(0,len(map_list)):
        count =0
        for m in range(0,len(normal_list)):
            if map_list[r] == normal_list[m]:
                count+=1

        print(map_list[r],':',count)

def find_count_in_list_by_get(normal_list,map_list):

    count_dict = dict()
    hash_map_dict = dict()

    for num in normal_list:
            count_dict[num] = count_dict.get(num,0)+1

    for num in map_list:
        if num <1 or num >10:
            print(num,':',0)
        else:
            print(num,":",count_dict.get(num,0))
    print('Count List:',hash_map_dict)

def find_count_in_list_by_list(normal_list,map_list):

    hash_list  = [0]*11
    # print(hash_list)
    for n in normal_list:
        if n >=0 and n <=10:
            hash_list[n]=  hash_list[n] + 1
    
    
    for m in map_list:
        if m>=0 and m<=10:
            print(m,":",hash_list[m])
        else:
            print(m,":",0)

if __name__=="__main__":
    normal_l=[2,3,1,1,3,5,4,4,3,1,5,5]
    map_l=[1,4,2,5,14,6]
    print("Jay Shree Ram")
    # find_count_in_list(normal_l,map_l)
    find_count_in_list_by_get(normal_l,map_l)
    find_count_in_list_by_list(normal_l, map_l)