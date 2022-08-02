import random

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
bot = Bot(token='', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)

data = {'make': 'Nokia'}


@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    name = query.from_user.id
    text = query.query
    ran = randint(1, 40)
    if f'{name}' in data:
        link = data[f'{name}']
    else:
        if ran <= 5:
            link = f'<i>Your dick size for today is:</i> <b>{ran}cm</b> 🤡'
            data[f'{name}'] = link
        elif 5 < ran <= 15:
            link = f'<i>Your dick size for today is:</i> <b>{ran}cm</b> 🤫'
            data[f'{name}'] = link
        elif 15 < ran <= 25:
            link = f'<i>Your dick size for today is:</i> <b>{ran}cm</b> 💪'
            data[f'{name}'] = link
        elif 25 < ran <= 35:
            link = f'<i>Your dick size for today is:</i> <b>{ran}cm</b> 😎'
            data[f'{name}'] = link
        elif 35 < ran <= 40:
            link = f'<i>Your dick size for today is:</i> <b>{ran}cm</b> 😍'
            data[f'{name}'] = link
    result_id: random.randint(1, 5) = hashlib.md5(text.encode()).hexdigest()

    articles = [types.InlineQueryResultArticle(
        id=result_id,
        title='🎲 Dick size',
        input_message_content=types.InputTextMessageContent(
            message_text=link, parse_mode=types.ParseMode.HTML))]
    await query.answer(articles, cache_time=1, is_personal=True)


executor.start_polling(dp, skip_updates=True)
