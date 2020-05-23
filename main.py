from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path
import os
from bookchecker import fetch_finded_books_info
import math
import shutil
from more_itertools import chunked


def clear_pages_dir():
    dirname = os.path.dirname(__file__)
    folder = os.path.join(dirname, 'pages')
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))



env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )


def render_pages(books_info):
    splitted_books = list(chunked(books_info, 10))
    amount_of_pages = math.ceil(len(books_info) / 10)
    template = env.get_template('template.html')

    for count, books in enumerate(splitted_books, 1):
        rendered_page = template.render(
            books=books,
            last_page_num=amount_of_pages,
            current_page=count,
        )
        with open('pages/index%s.html' % (count), 'w', encoding="utf8") as file:
            file.write(rendered_page)



def main():
    clear_pages_dir()
    root_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    dir_path = root_dir / 'pages'
    dir_path.mkdir(exist_ok=True)

    finded_books_info = fetch_finded_books_info()
    render_pages(finded_books_info)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()