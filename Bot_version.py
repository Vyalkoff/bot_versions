#!/usr/bin/python
# -*- coding: utf-8 -*-
import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command, CommandStart
from aiogram.utils.formatting import TextLink, Text, Bold, as_list, as_line, as_marked_section, as_key_value, HashTag
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hide_link
import autn
import Command_from_bot
import search_version
from chek_message_valid import valid
from data_for_auth import BOT_TOKEN

dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer('Можно посчитать сколько релизов нужно обновить до последней версии Бухгалтерии 3.0,'
                         'ввести версию релиза на данный момент. Пример:3.0.50.1, Ответ:С версии 3.0.50.1 '
                         'До последней версии необходимо обновить 12 ед.'
                         'Релизы: 3.0.51.1; 3.0.52.3;'
                         '3.0.53.2; 3.0.54.1; 3.0.55.1; 3.0.56.1;'
                         '3.0.57.1; 3.0.58.2; 3.0.59.1; 3.0.60.1;'
                         '3.0.61.1; 3.0.62.1;')


@dp.message(Command(commands='all_path'))
async def get_path(message: types.Message):
    await message.answer(f'Идет проверка патчей для последней версии.')
    path = Command_from_bot.update_path()
    for key, value in path.items():
        text = f'Для версии {key}\n'
        if value:
            for number, val in value.items():
                text += f'{number + 1}: Патч {val} - {val['description_column']}.Вышел: {val['date_column']}\n'
                print(text)
        else:
            text += 'Нет патчей'
    await message.answer(text)


# await message.answer(f'Проверяю патчи')
# await message.answer(f'Вышел новый патч для релиза ')


# @dp.message(Command(commands='path'))
# async def get_path(message: types.Message):
#     session = autn.authorization()
#     if session:
#         new_path = search_version.find_path_for_release(session, message.text)
#         await message.answer(f'Вышел новый патч для релиза {new_path}')
#     else:
#         await message.answer(f'Ошибка соедиения с сайтом, Обратится  к администратору')


@dp.message(Command(commands='update_release'))
async def update_release(message: types.Message):
    await message.answer('Получаю обновление информации о релизах....')
    await message.answer(Command_from_bot.update_release())


@dp.message(Command(commands='last_release'))
async def get_path(message: types.Message):
    await message.answer('Проверяю информацию о последнем релизе....')
    await message.answer(Command_from_bot.check_new_release())


@dp.message(Command(commands='update_path'))
async def get_path(message: types.Message):
    session = autn.authorization()
    if session:
        new_release = Command_from_bot.update_path(session)
        await message.answer(new_release)
    else:
        await message.answer(f'Ошибка соедиения с сайтом, Обратится  к администратору')


@dp.message(F.text)
async def send_echo(message: types.Message):
    version = valid(message.text)
    if version:
        try:
            counter, all_version = search_version.find_version(message.text)
        except Exception as er:
            await message.answer(f'Произошла ошибка подсчета')
            print(er)
        try:

            text_content = Text(
                f'С версии {message.text} До последней версии необходимо обновить{counter} ед. \n Релизы: ')
            content_link = []
            for key in all_version:
                content_link.append(TextLink(f'{key}; ', url=all_version[key][0]))

            content = as_line(text_content, *content_link, )

            await message.answer(**content.as_kwargs())
        except Exception as a:
            await message.answer(f'Произошла ошибка вывода релизов  Необходимо {counter}')
            print(a)

    else:
        text_error = f'Не правильно введена версия! Пример: 3.0.50.1 И только версии Бухгалтерии '
        await message.reply(text=text_error)


async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")

    # counter, all_version = search_version.find_version("3.0.54.1")
    # # content = as_list(TextLink(links, url=all_version[links][0])for links in all_version)
    # print(all_version)
    # # text = f'С версии {"3.0.54.1"} До последней версии {counter}\n Релизы {release}'

    # for key in all_version:
    #     gt = (**TextLink(body=all_version[key], url=all_version[key][0]).as_kwargs())

    # gt.as_kwargs()
    # # content.as_kwargs()
    # release = []
    # for key in all_version:
    #     release.append(TextLink(key, url=all_version[key][0]))
    #
    # rdp = ""
    # for i in release:
    #     for g in i:
    #         rdp += g
    # st_re = ",".join(release)
    # print(rdp)
    # else:
    #     text = f'Не правильно введена версия! Пример: 3.0.50.1 И только версии Бухгалтерии '
    #     print(text)
