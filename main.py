COLOR_GREEN = '\033[92m'
COLOR_OKCYAN = '\033[96m'
COLOR_OKBLUE = '\033[94m'
COLOR_WARNING = '\033[93m'
COLOR_FAIL = '\033[91m'
_COLOR_ENDC = '\033[0m'

_EX_1 = '1'
_ARRAY_EX = [_EX_1]

def get_text_color(text: str, color: str)-> str:
    return f'{color}{text}{_COLOR_ENDC}'

class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self) -> str:
        return f"Название: {self.title}, Автор: {self.author}, Страниц: {self.pages}"

    @staticmethod
    def is_fantasy(title: str) -> bool:
        title = title.lower()
        return "фантастика" in title or "фантастическая история" in title

    @classmethod
    def create_fantasy_book(cls, title: str, author: str, pages: int):
        return cls(f"фантастика {title}", author, pages)

    def __str__(self) -> str:
        return f"'{self.title}' - {self.author} ({self.pages} стр.)"

    def __eq__(self, other) -> bool:
        """сравнение количества страниц двух книг."""
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages == other.pages

    def __lt__(self, other) -> bool:
        """Сравнение: меньше ли страниц в текущей книге."""
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages < other.pages

    def __le__(self, other) -> bool:
        """Сравнение: меньше или равно страниц в текущей книге."""
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages <= other.pages

    def __gt__(self, other) -> bool:
        """Сравнение: больше ли страниц в текущей книге."""
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages > other.pages

    def __ge__(self, other) -> bool:
        """Сравнение: больше или равно страниц в текущей книге."""
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages >= other.pages



def main():
    while True:
        print(
            "\nЛарионов гр. 410з. Программирование на языках высокого уровня\n"
            "Индивидуальное задание №3 ООП. Вариант 3.\n"
            "Какую задачу выполнить: \n"
            f'''{get_text_color(f'{_EX_1}) ', COLOR_WARNING)}
            Напишите класс Book, содержащий информацию о книге, такую как
            название, автор, количество страниц. Реализуйте методы для получения
            информации о книге и статический метод для проверки, является ли
            книга фантастикой (есть слово «фантастика» или сочетание
            «фантастическая история» в названии), метод класса для создания книги
            в жанре фантастика (добавляется слово «фантастика» в начало
            названия), магический метод для представления книги в виде строки,
            магический метод для сравнения количества страниц двух книг.'''
        )
        select = input('Для выхода введите \'0\'\n')

        if select in _ARRAY_EX:
            globals()[f'_init_ex_{select}']()
        elif select == '0':
            break
        else:
            print(
                f'{get_text_color("Введен неверный номер задачи!", COLOR_FAIL)}'
            )

if __name__ == '__main__':
    main()