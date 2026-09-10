

def calculate_count_of_digits(num):
    count =0

    while num>0:
        count+=1
        num = num//10

    return count


if __name__== "__main__":
   print("Count Of Digits is: ",calculate_count_of_digits(898989))