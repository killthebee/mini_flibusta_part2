from livereload import Server, shell
import json
from jinja2 import Environment, FileSystemLoader, select_autoescape






def on_reload():

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    with open('books_info.json') as json_file:
        data = json.load(json_file)

    template = env.get_template('index.html')

    rendered_page = template.render(books=data)

    with open('indexx.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

server = Server()
server.watch('index.html', on_reload)
server.serve(root='.')
