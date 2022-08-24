n = int(input()) 
c = 'H'


for i in range(n):
    print((c*i).rjust(n-1)+c+(c*i).ljust(n-1))


for i in range(n+1):
    print((c*n).center(n*2)+(c*n).center(n*6))


for i in range((n+1)//2):
    print((c*n*5).center(n*6))    


for i in range(n+1):
    print((c*n).center(n*2)+(c*n).center(n*6))    


for i in range(n):
    print(((c*(n-i-1)).rjust(n)+c+(c*(n-i-1)).ljust(n)).rjust(n*6))

