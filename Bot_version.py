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
    await message.answer('hello')


@dp.message(Command(commands='new_path'))
async def get_path(message: types.Message):
    session = autn.authorization()
    if session:
        new_path = Command_from_bot.check_new_path(session)
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
async def update_release(message: types.Message):
    await message.answer('Идет информации о релизах....')
    await message.answer(Command_from_bot.update_release())


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

        # release = ""
        # for links in all_version:
        #     release = TextLink(links, url=all_version[links][0])
        #     break
        # release += f'<a href={all_version[links][0]}>{links}</a>'

        # content = as_list(TextLink(all_version[0], url=all_version[0][0]))
        # content = [list(**TextLink(key, url=all_version[key][0]).as_kwargs()) for key in all_version]
        # text = f'С версии {message.text} До последней версии {counter}\n Релизы '
        try:

            counter, all_version = search_version.find_version(message.text)
            text_content = Text(
                f'С версии {message.text} До последней версии необходимо обновить{counter} ед. \n Релизы: ')
            content_link = []
            for key in all_version:
                content_link.append(TextLink(f'{key}; ', url=all_version[key][0]))

            content = as_line(text_content, *content_link, )

            await message.answer(**content.as_kwargs())
        except Exception as a:
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
