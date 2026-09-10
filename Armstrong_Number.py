


def check_armstrong_number(num):
    no = num
    count =len(str(no))
    total =0
    # while no >0:
    #     no = no//10
    #     count +=1

    no = num
    while no > 0:
        d = no%10
        total += d**count
        no = no //10

    return total == num

if __name__ == "__main__":
    print("#Coder")
    print(check_armstrong_number(153))