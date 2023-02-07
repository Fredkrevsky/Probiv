import requests
import time
import config
import logging
from aiogram import Bot, Dispatcher, executor, types
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
def get_info(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
            '[IP]': response.get('query'),
            '[Провайдер]': response.get('isp'),
            '[Страна]': response.get('country'),
            '[Регион]': response.get('regionName'),
            '[Город]': response.get('city'),
            '[Индекс]': response.get('zip'),
            '[Широта]': response.get('lat'),
            '[Долгота]': response.get('lon'),
        }
        for k, v in data.items():
            print(f'{k} : {v}')


    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Приветствую')
    time.sleep(1)
    await message.answer('Введите IP-адрес:')

@dp.message_handler(content_types=['text']) 
async def probiv(message: types.Message): 
    ip = message.text  
    get_info(ip=ip)
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
