import os

def separate(list_of_strings):
    result_list = list()
    for string in list_of_strings:
        tokenised = list(string)
        odd = ''.join(tokenised[::2])
        even = ''.join(tokenised[1::2])
        result = ' '.join([odd, even])
        print(result)
        result_list.append(result)
    return result_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    test_cases = int(input().strip())

    strings = []

    for _ in range(test_cases):
        string = str(input().strip())
        strings.append(string)

    result = separate(strings)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
