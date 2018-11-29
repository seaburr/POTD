'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

test_1 = [3, 4, -1, 1]
test_2 = [1, 2, 0]
test_3 = []
test_4 = [100, 95, 3, -1]

'''
for each 
'''

def v1_lowest(input):
    output = None
    for i in range(0, len(input)):
        if input[i] + 1 > 0 and input[i] + 1 not in input:
            if output is None or input[i] + 1 < output:
                output = input[i] + 1
    return output



#v1_lowest(test_1)

print(test_1)
test_1.sort()
print(test_1)
print(v1_lowest(test_1))
print(v1_lowest(test_2))
print(v1_lowest(test_3))
print(v1_lowest(test_4))