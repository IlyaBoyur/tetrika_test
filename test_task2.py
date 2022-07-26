import pywikibot

from task2 import calculate_page_counts


def ascii_filter(page):
    """Accept page if it`s title contains ascii chars"""
    return all(word.isalpha() for word in page.title().split())


def no_filter(page):
    """Simply skip filtering"""
    return True


def any_attribute(page):
    """Use no page specific attribute"""
    return 'total'


if __name__ == '__main__':
    """Here example usage is showed"""
    site = pywikibot.Site('ru')
    print(calculate_page_counts(site))
    print(calculate_page_counts(site,
                                'Категория:Фильмы по алфавиту',
                                lambda page: True))
    print(calculate_page_counts(site,
                                'Категория:Телесериалы по алфавиту',
                                ascii_filter))
    print(calculate_page_counts(site, 'Категория:Автомобили по алфавиту',
                                no_filter,
                                any_attribute))
