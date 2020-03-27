from livereload import Server, shell
import json
from jinja2 import Environment, FileSystemLoader, select_autoescape

#lol

def on_reload():

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    with open('books_info.json') as json_file:
        data = json.load(json_file)

    last_page_num = 8
    for num in range(0, last_page_num):
        render_page(num, data, last_page_num, env)


def render_page(num, data, last_page_num, env):
    template = env.get_template('index.html')
    start_index = num * 10
    end_index = start_index + 10
    rendered_page = template.render(
        books=data[start_index:end_index],
        last_page_num=last_page_num,
        current_page=num + 1,
    )
    with open('pages/index%s.html'%(num + 1), 'w', encoding="utf8") as file:
        file.write(rendered_page)

server = Server()
server.watch('main.py', on_reload)
server.serve(root='.')
