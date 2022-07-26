# Задача №2.
# В нашей школе мы не можем разглашать персональные данные пользователей,
# но чтобы преподаватель и ученик смогли объяснить нашей поддержке,
# кого они имеют в виду (у преподавателей, например, часто учится
# несколько Саш), мы генерируем пользователям уникальные и
# легко произносимые имена. Имя у нас состоит из прилагательного,
# имени животного и двузначной цифры. В итоге получается, например,
# "Перламутровый лосось 77".
# Для генерации таких имен мы и решали следующую задачу:
# Получить с русской википедии список всех животных (https://inlnk.ru/jElywR)
# и вывести количество животных на каждую букву алфавита.
# Результат должен получиться в следующем виде:
# А: 642
# Б: 412
# В:....
import unicodedata
from collections import Counter
from typing import Callable, List, Tuple

import pywikibot
from pyuca import Collator
from pywikibot import pagegenerators
from tqdm import tqdm

CYRILLIC = 'CYRILLIC'
CATEGORY = 'Категория:Животные по алфавиту'
PROGRESS_INFO = 'Обработка страниц Wikipedia. {category}'


PageAttr = Callable[[pywikibot.Page], str]
PageFilter = Callable[[pywikibot.Page], bool]

def first_char_page_attribute(page: pywikibot.Page) -> str:
    """Specify page attribute: page title`s first character"""
    return page.title().split()[0][0].capitalize()


def noun_title_page_filter(page: pywikibot.Page) -> bool:
    """Specify page filter: page title`s first word is a cyrillic noun"""
    name = page.title().split()
    return (
        is_name_cyrillic(name) and not is_name_plural(name)
        and not is_name_adjective(name)
    )


def is_name_plural(name: List[str]) -> bool:
    """Examine name is cyrillic plural"""
    return name[0][-1] in ('ы', 'и')


def is_name_adjective(name: List[str]) -> bool:
    """Examine name is cyrillic adjective"""
    return name[0][-2:] in (
        'ие', 'ые', 'ий', 'ый', 'ой', 'ая', 'ое', 'ов'
    )


def is_name_cyrillic(name: List[str]) -> bool:
    """Examine name is cyrillic"""
    return CYRILLIC == unicodedata.name(name[0][0]).split()[0]


def calculate_page_counts(site: pywikibot.BaseSite,
                          category: str = CATEGORY,
                          page_filter: PageFilter = noun_title_page_filter,
                          page_attribute: PageAttr = first_char_page_attribute):
    """Calculate Wikipedia page counts by specified attribute.

    :param site: pywikibot.Site class instance
    :param category: page category which is examined
    :param page_filter: filter for pages in specified category. Defaults to
    "first word is a cyrillic noun" filter.
    :param page_attribute: attribute to be calculated for page. Defaults to
    first char in page`s title.
    """
    def sort_key(element: Tuple[str, int]) -> Tuple:
        """Encupsulates page_attribute sort key"""
        char, _ = element
        return Collator().sort_key(char)
    category_page = pywikibot.Category(site, title=category)
    page_generator = filter(
        page_filter,
        pagegenerators.CategorizedPageGenerator(category_page)
    )
    return sorted(Counter(
        page_attribute(page)
        for page in tqdm(page_generator,
                         desc=PROGRESS_INFO.format(category=category),
                         total=category_page.categoryinfo['pages'])
    ).items(), key=sort_key)


if __name__ == '__main__':
    site = pywikibot.Site('ru')
    for letter, count in calculate_page_counts(site):
        print(f'{letter}: {count}')
