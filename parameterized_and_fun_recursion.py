from typing import Any


def parameterized_fun(sum_val,i,n):

    if i >n:
        print('Sum:',sum_val)
        return

    parameterized_fun(sum_val+i,i+1,n)


def functional_recursion(sum_val) -> int: #in that we need return value

    if sum_val==1:
        return 1

    return sum_val+function_recursion(sum_val-1)


if __name__=="__main__":
    print('Jay Shree Ram')
    parameterized_fun(0,1,10)
    print('Fun_rec:',functional_recursion(10))