


def fact_num(num):

    if num==1:
        return 1
    return num*fact_num(num-1)




if __name__=="__main__":
    print("JAY SHREE RAM")
    ans = fact_num(5)
    print('FACTORIAL ANS:',ans)
