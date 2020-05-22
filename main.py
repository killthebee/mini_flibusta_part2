from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path
import os
from bookchecker import fetch_finded_books_info
import math


env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )


def render_pages(books_info):
    amount_of_pages = math.ceil(len(books_info) / 10)
    for num in range(0, amount_of_pages):
        render_page(num, books_info, amount_of_pages)


def render_page(num, data, last_page_num):
    template = env.get_template('template.html')
    start_index = num * 10
    end_index = start_index + 10
    rendered_page = template.render(
        books=data[start_index:end_index],
        last_page_num=last_page_num,
        current_page=num + 1,
    )
    with open('pages/index%s.html'%(num + 1), 'w', encoding="utf8") as file:
        file.write(rendered_page)


def main():
    root_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    dir_path = root_dir / 'pages'
    dir_path.mkdir(exist_ok=True)

    finded_books_info = fetch_finded_books_info()
    render_pages(finded_books_info)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()



if __name__ == '__main__':
    main()