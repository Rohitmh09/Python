


def get_fibonacci_series(a,b,num,li):

    if num==-1: #If num start 1,2,3... then set num==0
        return li

    li.append(a)
    return get_fibonacci_series(b,a+b,num-1,li)


#Print Exact N^th Fibonacci number logic= f(n) = f(n-1)+f(n-2)
#num = 9 final number= 34
#num(8) + num(7) = 21 + 13 =34 IF we get from 0
def get_fibonacci_num(num):

    if num ==0 or num ==1:
        return  num

    return get_fibonacci_num(num-1)+get_fibonacci_num(num-2)




if __name__=="__main__":
    print('JAY SHREE RAM')
    ans = get_fibonacci_series(0,1,9,[])
    print("Fibonacci List:",ans)

    fb_num = get_fibonacci_num(5)
    print('Final Fibonacci Num:',fb_num)