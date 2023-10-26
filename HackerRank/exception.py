n = int(input())
for i in range(n):
    try:
        divider, divisor = map(int, input().split(sep=" "))
        print(divider//divisor)
    except (ZeroDivisionError, ValueError) as e:
        print(f"Error Code: {e}")