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
_EX_5 = '6'

def get_text_color(text: str, color: str)-> str:
    return f'{color}{text}{_COLOR_ENDC}'

def is_number(str)-> bool:
    try:
        float(str)
        return True
    except ValueError:
        return False

def input_number(text: str, default_value: float = None, min: float = None, max: float = None)-> float:
    while True:
        number = input(f'{get_text_color(text, COLOR_WARNING)} ')
        if number == '':
            if default_value is not None:
                return default_value
            else:
                print(get_text_color(f"Введите число!", COLOR_FAIL))
        elif is_number(number):
            if min is not None and float(number) < min:
                print(get_text_color(f"Минимально допустимое число - {min}!", COLOR_FAIL))
            elif max is not None and float(number) > max:
                print(get_text_color(f"Максимально допустимое число - {max}!", COLOR_FAIL))
            else:
                return float(number)
        else:
            print(get_text_color(f"\"{number}\" - не число! Повторите ввод!", COLOR_FAIL))
            
    return 0.0

def input_string(text: str)-> str:
    while True:
        _string = input(f'{get_text_color(text, COLOR_WARNING)} ')
        if _string == '':
            print(get_text_color(f"Текст не должен быть пустым!", COLOR_FAIL))
        else:
            return _string
            
    return ''

class Book:
    title: str
    author: str
    pages: str
    
    def get_info(self) -> str:
        return f"Название: {self.title}, Автор: {self.author}, Страниц: {self.pages}"

    @staticmethod
    def is_fantasy(title: str) -> bool:
        title = title.lower()
        return "фантастика" in title or "фантастическая история" in title

    @classmethod
    def create_book(cls, title: str, author: str, pages: int):
        return cls(title, author, pages)

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


def action_add_book():
    title = input_string(text="Введите название книги: ").lower().capitalize()
    author = input_string(text="Введите автора книги: ").lower().capitalize()
    pages = int(input_number(text="Введите натуральное трехзначное число: ", min=0, max=9_999_999))
    book = Book()
    book.create_book(title=title, author=author, pages=pages)


_ARRAY_EX = {
    _EX_1: action_add_book
}

def main():
    while True:
        print(
            '''\nЛарионов гр. 410з. Программирование на языках высокого уровня\n"
            "Индивидуальное задание №3 ООП. Вариант 3.\n"
            "Какую задачу выполнить: \n\n
            Напишите класс Book, содержащий информацию о книге, такую как
            название, автор, количество страниц. Реализуйте методы для получения
            информации о книге и статический метод для проверки, является ли
            книга фантастикой (есть слово «фантастика» или сочетание
            «фантастическая история» в названии), метод класса для создания книги
            в жанре фантастика (добавляется слово «фантастика» в начало
            названия), магический метод для представления книги в виде строки,
            магический метод для сравнения количества страниц двух книг.\n\n
            '''
            f'''{get_text_color(f'{_EX_1}) ', COLOR_WARNING)}
            Добавить книгу в библиотеку\n
            {get_text_color(f'{_EX_2}) ', COLOR_WARNING)}
            Получить информацию о книге\n
            {get_text_color(f'{_EX_2}) ', COLOR_WARNING)}
            Проверить является ли книга фантастикой\n
            {get_text_color(f'{_EX_2}) ', COLOR_WARNING)}
            Добавить книгу в жанре фантастика\n
            {get_text_color(f'{_EX_2}) ', COLOR_WARNING)}
            Книга как строка\n
            {get_text_color(f'{_EX_2}) ', COLOR_WARNING)}
            Сравнить книги\n'''
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