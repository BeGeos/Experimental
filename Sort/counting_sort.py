"""
Implementing counting sort and Radix sort
"""

# start_list = [2, 13, 7, 1, 0, -4, 3, 4, 8]


def counting_sort(item):
    """Counting sort of a generic list of items.
    Only parameter an array of integers, it return a sorted array"""

    output = [*item]  # Copy of input list, doesn't change the original input
    count_list = [0 for i in range(min(output), max(output) + 1)]

    for j in output:
        count_list[j - min(output)] += 1

    for z in range(1, len(count_list)):
        count_list[z] += count_list[z - 1]

    for k in range(len(item)):
        position = count_list[item[k] - min(item)] - 1
        output[position] = item[k]
        count_list[item[k] - min(item)] -= 1

    return output

