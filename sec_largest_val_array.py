

li = [2,3,5,7,1,8]
large = float("-inf")
sec_large = float("-inf")

for i in range(len(li)): #TC=O(N) and SP=O(1) constant we only ise 2 values which not increase there size
    if li[i]>large:
        sec_large = large
        large = li[i]
    if large > li[i] and li[i]>sec_large:
        sec_large = li[i]

print('secomd largest:',sec_large)

    