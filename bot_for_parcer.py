import json
import time

from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from parcer import parce

bot = Bot(token='5577030759:AAGBfOqOkeBBo2hMV05BijLEqQ9ysqXpyzA')
dp = Dispatcher(bot)

# создание конпок
wheel_button = KeyboardButton("Колеса")
body_button = KeyboardButton("Корпус")
back_button = KeyboardButton("Вернутся назад")

# создаие клавиатур
main_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
back_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

# добавление конпок в клавиатуру
main_kb.add("Корпуса")
main_kb.add("Колеса")
main_kb.add("Декали")
main_kb.add("Ракетные ускорения")
main_kb.add("Анимация гола")
main_kb.add("Шапки")
main_kb.add("Виды красок")
main_kb.add("Антенны")
main_kb.add("Ракетные следы")
main_kb.add("Баннеры")
main_kb.add("Звуки мотора")
main_kb.add("Обводки аватара")

back_kb.add("Вернутся назад")


@dp.message_handler(commands='start')
async def main_msg(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Привет, выбери категорию чтобы начать', reply_markup=main_kb)


@dp.message_handler(text='Колеса')
async def wheels(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Пожалуйста, подождите')

    parce(['c2', 'wheels'])
    with open('result.json', 'r') as file:
        data = json.load(file)
    for dic in data:
        name = dic.get('name_item')
        cost = dic.get('cost')
        trade_link = dic.get('trade_link')
        png_link = dic.get('png_link')
        # print(name, cost, trade_link, end='\n')

        await bot.send_message(chat_id=message.chat.id, text=f'Название: {name}\nСтоимость: {cost}\n{trade_link}')
        await bot.send_photo(chat_id=message.chat.id, photo=png_link, reply_markup=back_kb)
        # time.sleep(2)


@dp.message_handler(text='Корпуса')
async def bodies(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Пожалуйста, подождите')

    parce(['c1', 'bodies'])
    with open('result.json', 'r') as file:
        data = json.load(file)
    for dic in data:
        name = dic.get('name_item')
        cost = dic.get('cost')
        trade_link = dic.get('trade_link')
        png_link = dic.get('png_link')
        # print(name, cost, trade_link, end='\n')

        await bot.send_message(chat_id=message.chat.id, text=f'Название: {name}\nСтоимость: {cost}\n{trade_link}')
        await bot.send_photo(chat_id=message.chat.id, photo=png_link, reply_markup=back_kb)
        time.sleep(2)


@dp.message_handler(text='Декали')
async def decals(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Пожалуйста, подождите')

    parce(['c6', 'decals'])
    with open('result.json', 'r') as file:
        data = json.load(file)
    for dic in data:
        name = dic.get('name_item')
        cost = dic.get('cost')
        trade_link = dic.get('trade_link')
        png_link = dic.get('png_link')
        # print(name, cost, trade_link, end='\n')

        await bot.send_message(chat_id=message.chat.id, text=f'Название: {name}\nСтоимость: {cost}\n{trade_link}')
        await bot.send_photo(chat_id=message.chat.id, photo=png_link, reply_markup=back_kb)
        # time.sleep(2)


@dp.message_handler(text='Ракетные ускорения')
async def boosts(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Пожалуйста, подождите')

    parce(['c3', 'boosts'])
    with open('result.json', 'r') as file:
        data = json.load(file)
    for dic in data:
        name = dic.get('name_item')
        cost = dic.get('cost')
        trade_link = dic.get('trade_link')
        png_link = dic.get('png_link')
        # print(name, cost, trade_link, end='\n')

        await bot.send_message(chat_id=message.chat.id, text=f'Название: {name}\nСтоимость: {cost}\n{trade_link}')
        await bot.send_photo(chat_id=message.chat.id, photo=png_link, reply_markup=back_kb)
        # time.sleep(2)


@dp.message_handler(text='Анимация гола')
async def goal(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Пожалуйста, подождите')

    parce(['c10', 'explosions'])
    with open('result.json', 'r') as file:
        data = json.load(file)
    for dic in data:
        name = dic.get('name_item')
        cost = dic.get('cost')
        trade_link = dic.get('trade_link')
        png_link = dic.get('png_link')
        # print(name, cost, trade_link, end='\n')

        await bot.send_message(chat_id=message.chat.id, text=f'Название: {name}\nСтоимость: {cost}\n{trade_link}')
        await bot.send_photo(chat_id=message.chat.id, photo=png_link, reply_markup=back_kb)
        # time.sleep(2)


@dp.message_handler(text='Шапки')
async def toppers(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Пожалуйста, подождите')

    parce(['c4', 'toppers'])
    with open('result.json', 'r') as file:
        data = json.load(file)
    for dic in data:
        name = dic.get('name_item')
        cost = dic.get('cost')
        trade_link = dic.get('trade_link')
        png_link = dic.get('png_link')
        # print(name, cost, trade_link, end='\n')

        await bot.send_message(chat_id=message.chat.id, text=f'Название: {name}\nСтоимость: {cost}\n{trade_link}')
        await bot.send_photo(chat_id=message.chat.id, photo=png_link, reply_markup=back_kb)
        # time.sleep(2)


@dp.message_handler(text='Виды красок')
async def paint(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Пожалуйста, подождите')

    parce(['c8', 'paints'])
    with open('result.json', 'r') as file:
        data = json.load(file)
    for dic in data:
        name = dic.get('name_item')
        cost = dic.get('cost')
        trade_link = dic.get('trade_link')
        png_link = dic.get('png_link')
        # print(name, cost, trade_link, end='\n')

        await bot.send_message(chat_id=message.chat.id, text=f'Название: {name}\nСтоимость: {cost}\n{trade_link}')
        await bot.send_photo(chat_id=message.chat.id, photo=png_link, reply_markup=back_kb)
        # time.sleep(2)


@dp.message_handler(text='Антенны')
async def antenas(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Пожалуйста, подождите')

    parce(['c5', 'toppers'])
    with open('result.json', 'r') as file:
        data = json.load(file)
    for dic in data:
        name = dic.get('name_item')
        cost = dic.get('cost')
        trade_link = dic.get('trade_link')
        png_link = dic.get('png_link')
        # print(name, cost, trade_link, end='\n')

        await bot.send_message(chat_id=message.chat.id, text=f'Название: {name}\nСтоимость: {cost}\n{trade_link}')
        await bot.send_photo(chat_id=message.chat.id, photo=png_link, reply_markup=back_kb)
        # time.sleep(2)


@dp.message_handler(text='Ракетные следы')
async def rockets(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Пожалуйста, подождите')

    parce(['c9', 'trails'])
    with open('result.json', 'r') as file:
        data = json.load(file)
    for dic in data:
        name = dic.get('name_item')
        cost = dic.get('cost')
        trade_link = dic.get('trade_link')
        png_link = dic.get('png_link')
        # print(name, cost, trade_link, end='\n')

        await bot.send_message(chat_id=message.chat.id, text=f'Название: {name}\nСтоимость: {cost}\n{trade_link}')
        await bot.send_photo(chat_id=message.chat.id, photo=png_link, reply_markup=back_kb)
        # time.sleep(2)


@dp.message_handler(text='Баннеры')
async def banners(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Пожалуйста, подождите')

    parce(['c11', 'banners'])
    with open('result.json', 'r') as file:
        data = json.load(file)
    for dic in data:
        name = dic.get('name_item')
        cost = dic.get('cost')
        trade_link = dic.get('trade_link')
        png_link = dic.get('png_link')
        # print(name, cost, trade_link, end='\n')

        await bot.send_message(chat_id=message.chat.id, text=f'Название: {name}\nСтоимость: {cost}\n{trade_link}')
        await bot.send_photo(chat_id=message.chat.id, photo=png_link, reply_markup=back_kb)
        # time.sleep(2)


@dp.message_handler(text='Звуки мотора')
async def engine(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Пожалуйста, подождите')

    parce(['c12', 'engines'])
    with open('result.json', 'r') as file:
        data = json.load(file)
    for dic in data:
        name = dic.get('name_item')
        cost = dic.get('cost')
        trade_link = dic.get('trade_link')
        png_link = dic.get('png_link')
        # print(name, cost, trade_link, end='\n')

        await bot.send_message(chat_id=message.chat.id, text=f'Название: {name}\nСтоимость: {cost}\n{trade_link}')
        await bot.send_photo(chat_id=message.chat.id, photo=png_link, reply_markup=back_kb)
        # time.sleep(2)


@dp.message_handler(text='Обводки аватара')
async def wheels(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Пожалуйста, подождите')

    parce(['c13', 'borders'])
    with open('result.json', 'r') as file:
        data = json.load(file)
    for dic in data:
        name = dic.get('name_item')
        cost = dic.get('cost')
        trade_link = dic.get('trade_link')
        png_link = dic.get('png_link')
        # print(name, cost, trade_link, end='\n')

        await bot.send_message(chat_id=message.chat.id, text=f'Название: {name}\nСтоимость: {cost}\n{trade_link}')
        await bot.send_photo(chat_id=message.chat.id, photo=png_link, reply_markup=back_kb)
        time.sleep(2)


@dp.message_handler(text='Вернутся назад')
async def back(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, reply_markup=main_kb, text='Выбери категорию')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
