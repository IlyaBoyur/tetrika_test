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


def intervals_intersection(inter1, inter2, inter3) -> int:
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
    
    new_inter = intersections(make_pairs(inter1), make_pairs(inter2))
    result = intersections(new_inter, make_pairs(inter3))
    return sum(right - left for left, right in result)


def appearance(intervals: Dict[str, List[int]]) -> int:
    """Returns intersection for lesson, pupil and tutor"""
    lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']
    cleaned = intervals_clean([lesson, pupil, tutor])
    return intervals_intersection(cleaned[0], cleaned[1], cleaned[2])


if __name__ == '__main__':
    data = {'lesson': (1594692000, 1594695600),
            'pupil': (1594692033, 1594696347),
            'tutor': (1594692017, 1594692066, 1594692068, 1594696341)}
    expected = 3565
    actual = appearance(data)
    assert actual == expected, f'Error: got {actual}, expected {expected}'
