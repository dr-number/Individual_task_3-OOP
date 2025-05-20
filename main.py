from sqlalchemy import create_engine, Column, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import List, Optional

COLOR_GREEN = '\033[92m'
COLOR_OKCYAN = '\033[96m'
COLOR_OKBLUE = '\033[94m'
COLOR_WARNING = '\033[93m'
COLOR_FAIL = '\033[91m'
_COLOR_ENDC = '\033[0m'

_EX_1 = '1'
_EX_2 = '2'
_EX_3 = '3'
_EX_4 = '4'
_EX_5 = '5'
_EX_6 = '6'

Base = declarative_base()
engine = create_engine('sqlite:///library.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    pages = Column(Integer)

    def get_info(self) -> str:
        return f"Название: {self.title}, Автор: {self.author}, Страниц: {self.pages}"

    @staticmethod
    def is_fantasy(title: str) -> bool:
        book = session.query(Book).filter(func.lower(Book.title) == func.lower(title)).first()
        if not book:
            return None
    
        title = title.lower()
        return "фантастика" in title or "фантастическая история" in title

    @classmethod
    def create_book(cls, title: str, author: str, pages: int) -> 'Book':
        book = cls(title=title, author=author, pages=pages)
        session.add(book)
        session.commit()
        return book

    @classmethod
    def create_fantasy_book(cls, title: str, author: str, pages: int) -> 'Book':
        return cls.create_book(f"фантастика {title}", author, pages)

    @classmethod
    def get_all_books(cls) -> List['Book']:
        return session.query(cls).all()

    @classmethod
    def find_by_title(cls, title: str) -> Optional['Book']:
        return session.query(cls).filter(func.lower(cls.title) == func.lower(title)).first()

    def __str__(self) -> str:
        return f"'{self.title}' - {self.author} ({self.pages} стр.)"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages == other.pages

    def __lt__(self, other) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages < other.pages

    def __le__(self, other) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages <= other.pages

    def __gt__(self, other) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages > other.pages

    def __ge__(self, other) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages >= other.pages

# Создаем таблицы
Base.metadata.create_all(engine)

def get_text_color(text: str, color: str) -> str:
    return f'{color}{text}{_COLOR_ENDC}'

def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False

def input_number(text: str, default_value: float = None, min: float = None, max: float = None) -> float:
    while True:
        number = input(f'{get_text_color(text, COLOR_WARNING)} ')
        if number == '':
            if default_value is not None:
                return default_value
            print(get_text_color("Введите число!", COLOR_FAIL))
        elif is_number(number):
            num = float(number)
            if min is not None and num < min:
                print(get_text_color(f"Минимально допустимое число - {min}!", COLOR_FAIL))
            elif max is not None and num > max:
                print(get_text_color(f"Максимально допустимое число - {max}!", COLOR_FAIL))
            else:
                return num
        else:
            print(get_text_color(f"\"{number}\" - не число! Повторите ввод!", COLOR_FAIL))

def input_string(text: str) -> str:
    while True:
        _string = input(f'{get_text_color(text, COLOR_WARNING)} ')
        if _string == '':
            print(get_text_color("Текст не должен быть пустым!", COLOR_FAIL))
        else:
            return _string



def action_add_book():
    title = input_string("Введите название книги: ")
    author = input_string("Введите автора книги: ")
    pages = int(input_number("Введите количество страниц: ", min=1, max=9999))
    Book.create_book(title, author, pages)
    print(get_text_color("Книга успешно добавлена!", COLOR_GREEN))

def action_show_books():
    books = Book.get_all_books()
    if not books:
        print(get_text_color("В библиотеке нет книг!", COLOR_WARNING))
    else:
        for book in books:
            print(book)

def action_check_fantasy():
    action_show_books()
    title = input_string("Введите название книги для проверки: ")
    is_fantasy = Book.is_fantasy(title)
    if is_fantasy is None:
        print(get_text_color("Книга не найдена", COLOR_FAIL))
    elif is_fantasy:
        print(get_text_color("Это фантастика!", COLOR_GREEN))
    else:
        print(get_text_color("Это не фантастика.", COLOR_FAIL))

def action_add_fantasy_book():
    title = input_string("Введите название книги: ")
    author = input_string("Введите автора книги: ")
    pages = int(input_number("Введите количество страниц: ", min=1, max=9999))
    Book.create_fantasy_book(title, author, pages)
    print(get_text_color("Фантастическая книга добавлена!", COLOR_GREEN))

def action_compare_books():
    action_show_books()
    title1 = input_string("Введите название первой книги: ")
    book1 = Book.find_by_title(title1)
    if not book1:
        print(get_text_color(f"Книга '{title1}' не найдена!", COLOR_FAIL))
        return

    title2 = input_string("Введите название второй книги: ")
    book2 = Book.find_by_title(title2)
    if not book2:
        print(get_text_color(f"Книга '{title2}' не найдена!", COLOR_FAIL))
        return

    if book1 > book2:
        print(get_text_color(f"В книге '{book1.title}' больше страниц, чем в '{book2.title}'", COLOR_OKCYAN))
    elif book1 < book2:
        print(get_text_color(f"В книге '{book1.title}' меньше страниц, чем в '{book2.title}'", COLOR_OKCYAN))
    else:
        print(get_text_color(f"Обе книги имеют одинаковое количество страниц", COLOR_OKCYAN))

# Меню действий
_ARRAY_EX = {
    _EX_1: action_add_book,
    _EX_2: action_show_books,
    _EX_3: action_check_fantasy,
    _EX_4: action_add_fantasy_book,
    _EX_5: lambda: print(get_text_color("Для вывода книги как строки просто используйте print(book)", COLOR_OKBLUE)),
    _EX_6: action_compare_books
}

def main():
    while True:
        print(f'''
        {get_text_color('Ларионов гр. 410з. Программирование на языках высокого уровня', COLOR_GREEN)}
        {get_text_color('Индивидуальное задание №3 ООП. Вариант 3.', COLOR_GREEN)}\n\n
        Напишите класс Book, содержащий информацию о книге, такую как
        название, автор, количество страниц. Реализуйте методы для получения
        информации о книге и статический метод для проверки, является ли
        книга фантастикой (есть слово «фантастика» или сочетание
        «фантастическая история» в названии), метод класса для создания книги
        в жанре фантастика (добавляется слово «фантастика» в начало
        названия), магический метод для представления книги в виде строки,
        магический метод для сравнения количества страниц двух книг.
        {get_text_color('Библиотека книг', COLOR_GREEN)}

        {get_text_color(f'{_EX_1}) ', COLOR_WARNING)}Добавить книгу в библиотеку
        {get_text_color(f'{_EX_2}) ', COLOR_WARNING)}Показать все книги
        {get_text_color(f'{_EX_3}) ', COLOR_WARNING)}Проверить является ли книга фантастикой
        {get_text_color(f'{_EX_4}) ', COLOR_WARNING)}Добавить книгу в жанре фантастика
        {get_text_color(f'{_EX_5}) ', COLOR_WARNING)}Книга как строка
        {get_text_color(f'{_EX_6}) ', COLOR_WARNING)}Сравнить книги
        ''')
        select = input('Для выхода введите \'0\'\n')

        if select in _ARRAY_EX:
            _ARRAY_EX[select]()
        elif select == '0':
            break
        else:
            print(get_text_color("Введен неверный номер задачи!", COLOR_FAIL))

if __name__ == '__main__':
    main()