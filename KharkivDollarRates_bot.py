from time import ctime, sleep
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import message
from aiogram.utils import executor
from random import randint
import os, hashlib, logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
bot = Bot(token='', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)

url = urlopen("https://finance.i.ua/market/harkov/usd/?").read().decode('utf-8')
bs = BeautifulSoup(url, 'html.parser')


class DB:
    @classmethod
    def show_rates(cls):
        result = []
        for i in bs.find(lambda tag: tag.name == 'table'):
            for j in i.find_all_next('tbody'):
                for tr in j.find_all_next('tr'):
                    result.append(tr)
        str_list = []
        for i in result:
            str_list.append(
                f"Время: {str(i.find_next('time').next)}, Курс: {str(i['data-ratio'])}, Сума {str(i['data-amount'])}\n{i.find_all_next('td')[5].text}")
        return sorted(str_list, key=lambda x: (int(x[7:9]), int(x[10:12])), reverse=True)


@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    text = query.query
    link = [i for i in DB.show_rates()[0:6]]
    result_id: random.randint(1, 5) = hashlib.md5(text.encode()).hexdigest()

    articles = [types.InlineQueryResultArticle(
        id=result_id,
        title='💲 KharkivDollarRates',
        input_message_content=types.InputTextMessageContent(
            message_text='\n\n'.join(link), parse_mode=types.ParseMode.HTML))]

    await query.answer(articles, cache_time=1, is_personal=True)

executor.start_polling(dp, skip_updates=True)
