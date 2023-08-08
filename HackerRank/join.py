def split_and_join(line):
    word_list = line.split(" ")
    result = "-".join(word_list)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
