'''

Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

test_1 = [1, 2, 3, 4, 5]
test_2 = [3, 2, 1]


# Problem solved with nested for loops.
def multiply_list(number_list):
    output_list = []
    for i in range(0, len(number_list)):
        curr = 1
        tmp_list = number_list.copy()
        tmp_list.pop(i)
        for j in range(0, len(tmp_list)):
            curr = curr * tmp_list[j]
        output_list.append(curr)
    return output_list


# Attempting to solve this problem using recursion and without division.
def multiply_list_recurse(current_index, input_list=[], output_list=[]):
    if not current_index >= len(input_list):
        output_list.insert(current_index, 1)
        for i in range(0, len(input_list)):
            if not current_index == i:
                output_list[current_index] = output_list[current_index] * input_list[i]
        current_index += 1
        multiply_list_recurse(current_index, input_list, output_list)
    return output_list


# Same as above, but without needing an index val passed.
def multiply_list_recurse_v2(input_list=[], output_list=[]):
    if not len(output_list) >= len(input_list):
        output_list.insert(len(output_list), 1)
        for i in range(0, len(input_list)):
            if not (len(output_list) - 1) == i:
                output_list[(len(output_list) - 1)] = output_list[(len(output_list) - 1)] * input_list[i]
        multiply_list_recurse_v2(input_list, output_list)
    return output_list


print(multiply_list(test_1))
print(multiply_list(test_2))

print(multiply_list_recurse(0, test_1, []))
print(multiply_list_recurse(0, test_2, []))
print(multiply_list_recurse(0, [], []))

print(multiply_list_recurse_v2(test_1, []))
print(multiply_list_recurse_v2(test_2, []))
print(multiply_list_recurse_v2([], []))