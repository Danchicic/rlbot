import requests
from bs4 import BeautifulSoup
import re
import json

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.53'
}
result_data = []


def get_items(url):
    global name_item, link_png, link_trade, cost
    name_item = []
    link_png = []
    link_trade = []
    cost = []

    # src = requests.get(url=url, headers=headers)

    # with open('index.html', encoding='utf-8', mode='w') as file:
    #     file.write(src.text)

    with open('index.html', encoding='utf-8', mode='r') as file:
        src = file.read()
    page = BeautifulSoup(src, 'lxml')

    card = page.find_all('div', class_='rlg-trade__content')
    for j, block in enumerate(card):
        action = page.find_all('div', class_='rlg-trade__actions')
        items_has = block.find('div', class_="rlg-trade__itemshas").find_all('div', class_=re.compile('--hover'))
        items_want = block.find('div', class_="rlg-trade__itemswants").find_all('div', class_=re.compile('--hover'))
        if len(items_want) == len(items_has):
            action = page.find_all('div', class_='rlg-trade__actions')
            for i in range(len(items_want)):
                item_mean = items_has[i].find('a', class_='rlg-btn-primary --small').get('href').split('/')[2]
                items_want_mean = items_want[i].find('h2', class_='rlg-item__name').text
                if (item_mean == category[1]) and (items_want_mean == 'Credits'):
                    result_data.append(
                        {
                            'name_item': items_has[i].find('h2', class_='rlg-item__name').text,
                            'png_link': f"https://rocket-league.com{items_has[i].find('img').get('src')}",
                            'trade_link': f"https://rocket-league.com{action[j].find('ul', class_='rlg-more rlg-trade__more').find('a').get('href')}",
                            'cost': items_want[i].find('div', class_=re.compile('--quantity')).text.replace('\n',
                                                                                                            '').strip()
                        }
                    )
    with open('result.json', 'w') as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)


def parce(item_id):
    global category
    category = item_id
    get_items(
        f'https://rocket-league.com/trading?filterItem={category[0]}&filterCertification=0&filterPaint=0&filterSeries=A&filterRarity=A&filterMinCredits=0&filterMaxCredits=100000&filterSearchType=1&filterItemType=0')


parce(['c2', 'wheels'])
