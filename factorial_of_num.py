

def factorial_num(num):

    list_fact =[]
    index=0
    for i in range(1,(num//2+1)):
        if  num % i == 0  :
            # list_fact.append(i)
            list_fact.append(i)

    list_fact.append(num)

    print("Factorials are:",list_fact)


def fact_num_with_root_value(num):
    list_fact=set()

    for i in range(1,int(num**0.5)+1): # num**05 == used to find square root Time Complexity= O(rootN)
        if num%i==0:
            list_fact.add(i)
            if i != num//1:
                list_fact.add(num//i)
    print("With root:",sorted(list_fact)) # time complexity of sorted O(NlogN) total = O(rootN) + O(NlogN)



if __name__ =="__main__":
    print("Jay Shree Ram")
    factorial_num(125)
    fact_num_with_root_value(125)