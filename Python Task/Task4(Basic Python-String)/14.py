def merge_the_tools(string, k):
    # your code goes here
           
    for i in range(0,len(string),k):
        new_str = ''
        for j in string[i:i+k]:
            if j not in new_str:
                new_str += j
        print(new_str)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)