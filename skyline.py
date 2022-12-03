"""
Imagine a skyline of buildings and you were standing in front of them at ground level 0. How many of these buildings could you see?
Given a list [-1, 1, 3, 7, 7, 3], determine which values could be "seen." Output: [1,3,7]
pair programmed with Duyuan, this question is pretty easy.
"""
def skyline(building_list):
    temp_max = 0
    can_see = []
    for building in building_list:
        if building > temp_max:
            can_see.append(building)
            temp_max = building

    return can_see

print(skyline([-1, 1, 3, 7, 7, 3]))
print(skyline([-1, 3, 2, 7, 6, 8]))
