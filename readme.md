## Ларионов гр. 410з. Программирование на языках высокого уровня
## Индивидуальное задание №3 ООП. Вариант 3.
    Напишите класс Book, содержащий информацию о книге, такую как
    название, автор, количество страниц. Реализуйте методы для получения
    информации о книге и статический метод для проверки, является ли
    книга фантастикой (есть слово «фантастика» или сочетание
    «фантастическая история» в названии), метод класса для создания книги
    в жанре фантастика (добавляется слово «фантастика» в начало
    названия), магический метод для представления книги в виде строки,
    магический метод для сравнения количества страниц двух книг.

**Добавление книг**
<figure>
   <p align="center">Главное меню и задание</p>
   <p align="center">
      <img src="https://github.com/dr-number/Individual_task_3-OOP/blob/main/for_readme/1-main-menu.png">
   </p>
</figure>
<figure>
   <p align="center">Добавляем книгу</p>
   <p align="center">
      <img src="https://github.com/dr-number/Individual_task_3-OOP/blob/main/for_readme/2-add-book.png">
   </p>
</figure>
<figure>
   <p align="center">Добавляем книгу жанра фантастика</p>
   <p align="center">
      <img src="https://github.com/dr-number/Individual_task_3-OOP/blob/main/for_readme/3-add-fantastic-book.png">
   </p>
</figure>

**Просмотр книг**
<figure>
   <p align="center">Книги и БД</p>
   <p align="center">
      <img src="https://github.com/dr-number/Individual_task_3-OOP/blob/main/for_readme/4-show-all-books.png">
   </p>
</figure>

**Является ли книга фантастикой**
<figure>
   <p align="center">Книга не найдена и не является фантастикой</p>
   <p align="center">
      <img src="https://github.com/dr-number/Individual_task_3-OOP/blob/main/for_readme/6-check-fantastic-not.png">
   </p>
</figure>
<figure>
   <p align="center">Книга является фантастикой</p>
   <p align="center">
      <img src="https://github.com/dr-number/Individual_task_3-OOP/blob/main/for_readme/7-check-fantastic-yes.png">
   </p>
</figure>

# Create venv:
    python3 -m venv venv

# Activate venv:
## In Windows:
    venv\Scripts\activate
     
## In macOS or Linux:
    source venv/bin/activate

# install library
    pip install -r requirements.txt

# start 
    ./venv/bin/python "main.py"
