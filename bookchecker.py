from os import listdir
from os.path import isfile, join
import os
import json


def fetch_finded_books_info():

    dirname = os.path.dirname(__file__)
    mypath = os.path.join(dirname, 'books')
    mypath_two = os.path.join(dirname, 'books_info.json')
    with open(mypath_two) as json_file:
        books_info = json.load(json_file)

    finded_books_info = []
    for filename in listdir(mypath):
        if isfile(join(mypath, filename)):
            title = filename[:-4]
            img_path = '../' + 'images/' + title + '.jpg'
            book_path = '../' + 'books/' + filename
            finded_book_info = {}
            for book_info in books_info:
                if book_info['title'] == title:
                    finded_book_info['author'] = book_info['author']
                    finded_book_info['genres'] = book_info['genres']
                    break
            finded_book_info['title'] = title
            finded_book_info['img_path'] = img_path
            finded_book_info['book_path'] = book_path
            finded_books_info.append(finded_book_info)
            continue
    print(finded_books_info)
    return finded_books_info







