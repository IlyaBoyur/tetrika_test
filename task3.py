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
from typing import Dict, List


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
        result.append(pairs)
    return result


def intervals_intersection(inter1, inter2, inter3) -> int:
    'Returns intervals intersection for linear (non curcular) time'
    # for interval in intervals:
    pairs = []
    for a1, a2 in inter1:
        for b1, b2 in inter2:
            if b1 < a2 and a1 < b2:
                # intersection with last interval
                pairs.append((max(a1, b1), min(a2, b2)))
    result = []
    for a1, a2 in pairs:
        for b1, b2 in inter3:
            if b1 < a2 and a1 < b2:
                # intersection with last interval
                result.append((max(a1, b1), min(a2, b2)))

    return sum(right - left for left, right in result)


def appearance(intervals: Dict[str, List[int]]) -> int:
    'Returns intersection for lesson, pupil and tutor'
    lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']
    res1, res2, res3 = intervals_clean([lesson, pupil, tutor])
    return intervals_intersection(res1, res2, res3)
