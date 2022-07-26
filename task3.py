# Задача №3.
# Когда пользователь заходит на страницу урока, мы сохраняем время его захода.
# Когда пользователь выходит с урока (или закрывает вкладку,
# браузер – в общем как-то разрывает соединение с сервером),
# мы фиксируем время выхода с урока. Время присутствия каждого пользователя
# на уроке хранится у нас в виде интервалов. В функцию передается словарь,
# содержащий три списка с таймстемпами (время в секундах):
#
# lesson – начало и конец урока
# pupil – интервалы присутствия ученика
# tutor – интервалы присутствия учителя
#
# Интервалы устроены следующим образом – это всегда список
# из четного количества элементов. Под четными индексами (начиная с 0)
# время входа на урок, под нечетными - время выхода с урока.
# Нужно написать функцию, которая получает на вход словарь с интервалами и
# возвращает время общего присутствия ученика и учителя на уроке (в секундах).
from typing import Dict, List, Tuple


def intervals_clean(intervals_collection: List[List[int]]) -> List[List[int]]:
    """Returns list of non overlapping intervals
    for intervals in intervals collection"""
    result = []
    for intervals in intervals_collection:
        pairs = []
        # add first pair
        pairs.append((*intervals[:2],))
        for left, right in zip(intervals[::2], intervals[1::2]):
            last_left, last_right = pairs[-1]
            if last_right > left and right > last_left:
                # union with last interval
                pairs[-1] = (min(last_left, left), max(last_right, right))
            else:
                # add new interval
                pairs.append((left, right),)
        # Flatten list of pairs
        result.append([value for sublist in pairs for value in sublist])
    return result


def intervals_intersection(intervals_collection: List[List[int]]) -> int:
    """Returns intervals intersection for linear (non circular) time"""
    def make_pairs(intervals: List[int]) -> List[Tuple[int, int]]:
        """Make interval pairs

        Use even list index as interval start
        use odd list index as invetrval end
        Note: input list has to have even number of elements
        """
        return [(left, right)
                for left, right in zip(intervals[::2], intervals[1::2])]

    def intersections(a: List[Tuple[int, int]], b: List[Tuple[int, int]]):
        """Calculate intersections between two input lists of intervals"""
        pairs = []
        for a1, a2 in a:
            for b1, b2 in b:
                if b1 < a2 and a1 < b2:
                    # intersection exists
                    pairs.append((max(a1, b1), min(a2, b2)))
        return pairs

    # Get all intersections for intervals collection
    result = make_pairs(intervals_collection[0])
    for intervals in intervals_collection[1:]:
        result = intersections(result, make_pairs(intervals))
    return sum(right - left for left, right in result)


def appearance(intervals: Dict[str, List[int]]) -> int:
    """Returns intersection for lesson, pupil and tutor"""
    lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']
    return intervals_intersection(intervals_clean([lesson, pupil, tutor]))


if __name__ == '__main__':
    def check_start_end(intervals):
        for start, end in zip(intervals[::2], intervals[1::2]):
            if end < start:
                raise RuntimeError(
                    f'Начало интервала {start} > конца интервала {end}'
                )
    while(True):
        print('Введите массив lesson. Формат: ')
        print('<start> <end>')
        lesson = [int(number) for number in input().split()]
        check_start_end(lesson)
        print('Введите массив pupil. Формат: ')
        print('<start1> <end1> <start2> <end2> ..')
        pupil = [int(number) for number in input().split()]
        check_start_end(pupil)
        print('Введите массив tutor. Формат: ')
        print('<start1> <end1> <start2> <end2> ..')
        tutor = [int(number) for number in input().split()]
        check_start_end(tutor)
        data = {'lesson': lesson,
                'pupil': pupil,
                'tutor': tutor}
        print(f'Пересечение интервалов: {appearance(data)}')
        
