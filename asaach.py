
# Great question. The .get() method is a safe way to retrieve a value from a dictionary.

# Your code:

# freq_list[num_list[i]] = freq_list.get(num_list[i], 0) + 1

# is commonly used to count frequencies.

# How .get() Works

# Syntax:

# dictionary.get(key, default_value)
# If key exists → return its value.
# If key does not exist → return default_value.

#   freq = {"Aman":1,"Rahul":2,"Sanjay":3,"Mohit":4}

#     print(freq.get('Aman','Not Found')) #-->1
#     print(freq.get('karan','Not Found')) #-->Not found



def count_fre_by_get(num_list,freq_list):
    for i in range(len(num_list)):
        freq_list[num_list[i]] = freq_list.get(num_list[i],0) + 1


if __name__ == "__main__":
    numlist = [1,2,3,2,4,1,2,3,4,3,2,1,5,4,3,1,2]
    frequence_list = dict()

    for i in range(len(numlist)):
        if numlist[i] in frequence_list:
            frequence_list[numlist[i]] = frequence_list[numlist[i]]+1
        else:
            frequence_list[numlist[i]]=1
    
    print(frequence_list)

    freq_list = dict()

    count_fre_by_get(numlist,freq_list)
    print('output by frequency by get()',freq_list)

  
