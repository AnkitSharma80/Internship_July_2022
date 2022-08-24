def minion_game(string):
    # your code goes here
    kevin  = 0
    stuart = 0
    str_len = len(string)
    for i in range (str_len):
        if s[i] in "AEIOU":
            kevin += (str_len) - i
        else:
            stuart += (str_len) - i
    
    if kevin > stuart:
        print("Kevin",kevin)
    elif kevin < stuart:
        print("Stuart",stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)