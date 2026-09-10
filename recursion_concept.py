
# below function is part of Head recursion because in that we do our job first (print('Jay Bajarang Bali',num))
# then we call our function (print_name(num-1))
def print_name_head_rec(num):

    print('Jay Bajarang Bali',num)  #our job

    if num > 0:
        print_name_head_rec(num-1) #Function calling
    else:
        return

# below function is part of Tail recursion because in that we do function call first then do our job
# most in case Tail Recursion run -1 time than Head Recursion

def print_name_tail_rec(num): #Tail Recursion
    if num > 0:
        print_name_tail_rec(num-1) #Function calling
    else:
        return
    print('Jay Bajarang Bali',num) #our job


if __name__=="__main__":
    print("Jay Shree Ram")
    # print_name_head_rec(7)
    print_name_tail_rec(7)