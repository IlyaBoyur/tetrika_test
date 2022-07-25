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


def binary_search_char_loop(array, left_char, right_char):
    """Returns left_char -> right_char transition index

    Time complexity: O(log(n))
    Memory space complexity: O(n)
    """
    if len(array) < 2:
        return -1
    left = 0
    right = len(array) - 1
    while (left + 1 < right):
        mid = (left + right) // 2
        if array[mid] == right_char:
            right = mid
        else:
            left = mid
    if array[left] == left_char and array[right] == right_char:
        return right
    return -1


def task(array: str) -> str:
    """1 -> 0

    Returns index of transition one to zero.
    Returns `-1` if no transition is found.
    """
    position = binary_search_char_loop(array, '1', '0')
    return f'OUT: {position}'


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(task(sys.argv[1]))
    else:
        print('Please provide array')
