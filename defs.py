import json
import httplib2


def get_png(url):
    h = httplib2.Http('.cache')
    response, content = h.request(url)
    with open(url.split("/")[-1], 'wb') as file:
        file.write(content)


def read_json():
    with open('result.json', 'r') as file:
        data = json.load(file)
    for dic in data:
        name = dic.get('name_item')
        cost = dic.get('cost')
        trade_link = dic.get('trade_link')
        png_url = dic.get('png_link')
        get_png(png_url)


