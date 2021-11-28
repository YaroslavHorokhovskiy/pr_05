"""4. Write a Python function that takes two lists and returns True if they
have at least one common member.
"""
def have_common(list1: list, list2: list) -> bool:
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                return True
    return False

# Інший спосіб:
# def have_common(list1: list, list2: list) -> bool:
#     if set(list1) & set(list2):
#         return True
#     else:
#         return False

list1 = [1, 4, 7, 10]
list2 = [12, 42, 'b', 4]

if have_common(list1, list2):
    print('Списки мають спільні елементи.')
else:
    print('Списки не мають спільних елементів.')
