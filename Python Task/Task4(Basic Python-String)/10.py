def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]

        print(deci.rjust(width),end=" ")
        print(octa.rjust(width),end=" ")
        print(hexa.rjust(width),end=" ")
        print(bina.rjust(width))
            
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)