def allLongestStrings(inputArray):
    arr_len = []
    for i in inputArray:
        arr_len.append(len(i))
        sort_my_list = sorted(arr_len)
        max_len = sort_my_list[-1]
        dictionary = list(zip(arr_len, inputArray))
        output_list = []
        for key,value in dictionary:
            if key == max_len:
                output_list.append(value)
            else:
                continue
    return output_list
