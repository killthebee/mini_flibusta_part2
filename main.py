from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
import argparse


env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )


parser = argparse.ArgumentParser(
        description='Choose how many pages you need'
    )
parser.add_argument('-l', '--last_page', help='Amount of pages')
args = parser.parse_args()


def render_pages(last_page_num):

    with open('books_info.json') as json_file:
        data = json.load(json_file)

    for num in range(0, last_page_num):
        render_page(num, data, last_page_num)


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


render_pages(int(args.last_page))
server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
