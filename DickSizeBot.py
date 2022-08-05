import random
import time
from time import ctime, sleep
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import message
from aiogram.utils import executor
from random import randint
import os, hashlib
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
bot = Bot(token='5172128174:AAEqCX6SfE-HHERZ7wH0Emls5oAvqTepQts', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)


class DB:
    data = {}
    counter_list = []

@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    async def data_cleaner():
        """to clean data at the next day"""
        while True:
            if len(DB.counter_list) < 7 and str(ctime().split()[0]) not in DB.counter_list:
                DB.counter_list.append(str(ctime().split()[0]))
                DB.data.clear()
                return
            elif len(DB.counter_list) == 7:
                DB.counter_list.clear()
                continue
            return

    await data_cleaner()
    name = query.from_user.id
    text = query.query
    ran = randint(1, 40)
    if f'{name}' in DB.data:
        link = DB.data[f'{name}']
    else:
        if ran <= 5:
            link = f'<i>Your dick size for today is:</i> <b>{ran}cm</b> 🤡'
            DB.data[f'{name}'] = link
        elif 5 < ran <= 15:
            link = f'<i>Your dick size for today is:</i> <b>{ran}cm</b> 🤫'
            DB.data[f'{name}'] = link
        elif 15 < ran <= 25:
            link = f'<i>Your dick size for today is:</i> <b>{ran}cm</b> 💪'
            DB.data[f'{name}'] = link
        elif 25 < ran <= 35:
            link = f'<i>Your dick size for today is:</i> <b>{ran}cm</b> 😎'
            DB.data[f'{name}'] = link
        elif 35 < ran <= 40:
            link = f'<i>Your dick size for today is:</i> <b>{ran}cm</b> 😍'
            DB.data[f'{name}'] = link
    result_id: random.randint(1, 5) = hashlib.md5(text.encode()).hexdigest()

    articles = [types.InlineQueryResultArticle(
        id=result_id,
        title='🎲 Dick size',
        input_message_content=types.InputTextMessageContent(
            message_text=link, parse_mode=types.ParseMode.HTML))]

    await query.answer(articles, cache_time=1, is_personal=True)

executor.start_polling(dp, skip_updates=True)
