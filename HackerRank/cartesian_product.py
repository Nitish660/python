set_A = [int(x) for x in input().split()]
set_B = [int(x) for x in input().split()]

result = [(a, b) for a in set_A for b in set_B]
print(" ".join(f"({a}, {b})" for a, b in result))
