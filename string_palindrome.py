


def check_palindrome(org_str,modify_str,left,right):

    if left>=right:
        # return org_str == ''.join(modify_str) #Convert list into string by join
        return True

    if modify_str[left] != modify_str[right]: #Time Complexity O(N/2) = O(N) Space Complexity = O(N) Stack size
        # modify_str[left],modify_str[right]=modify_str[right],modify_str[left] #If values are not match in short it is not palindrome
        return False
    return check_palindrome(org_str,modify_str,left+1,right-1)

def check_palindrome_org(org_str,left,right):

    if left>=right:
        return True

    if org_str[left] != org_str[right]: #Time Complexity O(N/2) = O(N) Space Complexity = O(N) Stack size
        return False
    return check_palindrome_org(org_str,left+1,right-1)



if __name__=="__main__":
    print("JAY SHREE RAM")
    str='AABCDEA'

    ans =check_palindrome(str,list(str),0,len(str)-1)
    ans2 = check_palindrome_org(list(str),0,len(str)-1)
    print('IS Palindrome:',ans)
    print('Is Ans2 Palindrome:',ans2)