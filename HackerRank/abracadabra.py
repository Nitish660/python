def mutate_string(string, position, character):
    # Convert the string to a list
    l = list(string)
    
    # Replace the character at the specified position
    l[position] = character
    
    # Join the list back into a string
    new_string = ''.join(l)
    
    return new_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)