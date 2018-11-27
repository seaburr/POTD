'''
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

number_list = [10, 15, 3, 7]
k = 17


# First attempt.
def find_k(number_list, k):
    for i in range(0, len(number_list)):
        curr = number_list[i]
        tmp = number_list.copy()
        tmp.pop(i)
        for j in range(0, len(tmp)):
            sum = curr + tmp[j]
            if sum == k:
                return True
        return False

def sum_exists(numbers, target):
    differences = {target - number for number in numbers}
    return bool(differences.intersection(numbers))



