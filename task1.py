# Задача №1.
# Дан массив чисел, состоящий из некоторого количества подряд идущих единиц,
# за которыми следует какое-то количество подряд идущих нулей:
# 111111111111111111111111100000000.
# Найти индекс первого нуля (то есть найти такое место,
# где заканчиваются единицы, и начинаются нули)
# def task(array):
#     pass

# print(task("111111111110000000000000000"))
# # >> OUT: 11
# …
import sys


def binary_search_char(array, left_char, right_char, left, right):
    """Returns left_char -> right_char transition index

    Time complexity: O(log(n))
    Memory space complexity: O(n)
    """
    if left + 1 == right:
        if array[left] == left_char and array[right] == right_char:
            return right
        return -1
    mid = (left + right) // 2
    if array[mid] == right_char:
        return binary_search_char(array, left_char, right_char, left, mid)
    else:
        return binary_search_char(array, left_char, right_char, mid, right)


def task(array: str) -> str:
    """1 -> 0

    Returns index of transition one to zero.
    Returns `-1` if no transition is found.
    """
    position = binary_search_char(array, '1', '0', 0, len(array) - 1)
    return f'OUT: {position}'


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(task(sys.argv[1]))
    else:
        print('Please provide array')
