from itertools import permutations

input_string, repeat = input().split()
perms = sorted(permutations(input_string, int(repeat)))

for perm in perms:
    print(''.join(perm))

    