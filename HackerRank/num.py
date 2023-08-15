def print_formatted(number):
    for i in range (1,n+1):
        print(f"{i}  { oct(i)[2:]}  { hex(i)[2:]}  { bin(i)[2:]} ")
         

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)