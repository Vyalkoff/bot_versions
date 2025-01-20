#!/usr/bin/python
# -*- coding: utf-8 -*-
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandStart

import autn
import check_up
import search_version
from chek_message_valid import valid
from data_for_auth import BOT_TOKEN

dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer('hello')


@dp.message(Command(commands='new_path'))
async def get_path(message: types.Message):
    session = autn.authorization()
    if session:
        new_path = check_up.check_new_path(session)
        await message.answer(f'Вышел новый патч для релиза {new_path}')
    else:
        await message.answer(f'Ошибка соедиения с сайтом, Обратится  к администратору')


@dp.message(Command(commands='path'))
async def get_path(message: types.Message):
    session = autn.authorization()
    if session:
        new_path = search_version.find_path_for_release(session, message.text)
        await message.answer(f'Вышел новый патч для релиза {new_path}')
    else:
        await message.answer(f'Ошибка соедиения с сайтом, Обратится  к администратору')


@dp.message(Command(commands='update_release'))
async def get_path(message: types.Message):
    session = autn.authorization()
    if session:
        new_release = check_up.check_new_release(session)
        await message.answer(new_release)
    else:
        await message.answer(f'Ошибка соедиения с сайтом, Обратится  к администратору')


@dp.message(Command(commands='update_path'))
async def get_path(message: types.Message):
    session = autn.authorization()
    if session:
        new_release = check_up.update_path(session)
        await message.answer(new_release)
    else:
        await message.answer(f'Ошибка соедиения с сайтом, Обратится  к администратору')


@dp.message()
async def send_echo(message: types.Message):
    version = valid(message.text)
    if version:
        counter, all_version = search_version.find_version(message.text)
        text = f'С версии {message.text} До последней версии {counter}\n Релизы {'! '.join(all_version)}'

        await message.reply(text=text)
    else:
        text = f'Не правильно введена версия! Пример: 3.0.50.1 И только версии Бухгалтерии '
        await message.reply(text=text)


async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
