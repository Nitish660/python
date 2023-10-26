def merge_the_tools(string, k):
    # your code goes here

    index = -1
    result = []

    for i in range(len(string)):
        if i % k == 0:
            tracker = {}
            result.append("")
            index += 1

        if string[i] not in tracker:
            tracker[string[i]] = 1
            result[index] += string[i]

    for i in result:
        print(i)