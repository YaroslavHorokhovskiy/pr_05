"""3. Write a Python program which accepts a sequence of commaseparated numbers
from user and generate a list and a tuple with those numbers.
Sample data: 3, 5, 7, 23
Output:
List: ['3', '5, '7, '23']
Tuple: ('3', '5', '7', '23')
"""
data = input('Введіть послідовність чисел, розділених комою: ')

data_list = [item.strip() for item in data.split(',')]
print(data_list)

data_tuple = tuple(data_list)
print(data_tuple)
