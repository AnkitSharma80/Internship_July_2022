def swap_case(s):
    swap=[]
    for i in range(len(s)):
        if (s[i].isupper())==True:
            swap.append(s[i].lower())
        elif (s[i].islower()==True):
            swap.append(s[i].upper())
        else:
            swap.append(s[i])    
        stri=''
    return stri.join(swap)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)