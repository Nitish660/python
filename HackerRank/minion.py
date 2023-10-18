def minion_game(string):
    # your code goes here
    v=0 #5 3 1
    c=0 #6 4 2

    string=string.upper()
    vov="aeiou".upper()
    string=string.upper()
    for i in range(0, len(string)):
        if string[i] in vov:
            v+=len(string)-i
        else:
            c+=len(string)-i
    if v>c:
        print("Kevin", v)
    elif c>v:
        print("Stuart", c)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)