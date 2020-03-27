# Сайт для спарсенных книг с сайта tululu.org

Этот скрипт создаёт верстку для сайта с книгами, скачанными в [предыдущей части проекта](https://github.com/killthebee/mini_flibusta).

### Как установить

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Пример запуска
Скачав скрипт, в коммандной строке запустите:
```
python main.py -l 5
```
В папке проекта появиться папка `pages` в которой лежат html файлы для сайта.

Описание агрументов ниже.

Прежде чем запустить это срипт необходимо раздобыть книги при помощи [bookDownloader](https://github.com/killthebee/mini_flibusta)
. Запустив его, на вашем компьютере должны появиться папки с текстами книг, обложками,
 а так же файл `books_info.json` с информацией о книгах. Папки трогать не надо. А вот json файл необходимо перенести в одну папку
 с `main.py` этого проекта.

### Аргументы

`-l` или `--last_page` Обозначает количество страниц сайта с книгами.  Имейте ввиду, что на одной странице можно разместить 
максимум 10 книг. 


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
