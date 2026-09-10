

def count_frequency_of_num(num):
    list_dict = dict()

    for i in range(0,len(num)): #Time Complexity = O(N)
        if num[i] in list_dict:
            list_dict[num[i]]+=1 #Value Update in Dictionary is happened in O(1)
        else:
            list_dict[num[i]] = 1
    return  list_dict

def count_of_freq_with_get(num):
    hash_map=dict()

    for i in range(0,len(num)):
        hash_map[num[i]] = hash_map.get(num[i],0)+1

    return hash_map

if __name__ =="__main__":
    num_list = [3,2,2,4,1,1,3,4,4]
    print("Jay shree Ram")
    print(count_frequency_of_num(num_list))
    print(count_of_freq_with_get(num_list))