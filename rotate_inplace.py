"""
Given a list [1, 2, 3, 4, 5] and a number n, rotate the items in the list n places over to the right. The output would be: [3, 4, 5, 1, 2].
pair_programmed with duyuan, she gave me the idea using fast-slow pointers
"""


def rotate_list(list, shift_by):
    # in-place: shift to the left if shift_by is negative
    # looping over the array
    index1 = 0 # pointer to the index of the element we want to move
    index2 = 0 # pointer to the index we are going to move to
    temp = list[0] # temp var carries the element that lost its seat
    counter = 0 # each element moves once

    while counter < len(list):
        # calculate index2's position
        index2 = (index1 + shift_by) % len(list)
        temp, list[index2] = list[index2], temp
        index1 = index2
        counter += 1

    return list

print(rotate_list([1, 2, 3, 4, 5], 3))
