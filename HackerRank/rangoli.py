def get_chars(n, size):
    line = ''
    mid = int(n/2)
    for i in range(0, mid + 1):
        line += chr(size - i + 96)
    for i in range(mid - 1, -1, -1):
        line += chr(size - i + 96)
    return '-'.join(line)

def print_rangoli(size):
    cols = 4*size - 3
    rows = 2*size - 1
    for i in range(1, rows + 1, 2):
        print(get_chars(i, size).center(cols, '-'))
    for i in range(rows - 2, -1, -2):
        print(get_chars(i, size).center(cols, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)