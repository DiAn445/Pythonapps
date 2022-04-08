import random

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import message
from aiogram.utils import executor
from random import randint
import os, hashlib
import logging

from telebot.types import User

logging.basicConfig(level=logging.INFO)

import asyncio
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

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
        elif ran > 5 and ran <= 15:
            link = f'<i>Your dick size for today is:</i> <b>{ran}cm</b> 🤫'
            data[f'{name}'] = link
        elif ran > 15 and ran <= 25:
            link = f'<i>Your dick size for today is:</i> <b>{ran}cm</b> 💪'
            data[f'{name}'] = link
        elif ran > 25 and ran <= 35:
            link = f'<i>Your dick size for today is:</i> <b>{ran}cm</b> 😎'
            data[f'{name}'] = link
        elif ran > 35 and ran <= 40:
            link = f'<i>Your dick size for today is:</i> <b>{ran}cm</b> 😍'
            data[f'{name}'] = link
    result_id: random.randint(1, 5) = hashlib.md5(text.encode()).hexdigest()

    articles = [types.InlineQueryResultArticle(
        id=result_id,
        title='🎲 Dick size',
        input_message_content=types.InputTextMessageContent(
            message_text=link, parse_mode=types.ParseMode.HTML))]
    await query.answer(articles, cache_time=1, is_personal=True)


executor.start_polling(dp, skip_updates=True, )
