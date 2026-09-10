
def find_freq(str1):
    index_chars = [0]*127

    for s in str1:
        ind_val = ord(s)
        index_chars[ind_val] = index_chars[ind_val] + 1
       

    for j in range(len(index_chars)):
        ind_char = chr(j)
        if index_chars[j]>0:
            print("space" if ind_char ==' ' else ind_char, ":", index_chars[j],end=", ")

if __name__ == "__main__":
    input_string = " amanra%%jve rmazz@##"
    find_freq(input_string)
    

    