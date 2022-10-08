import logging
from aiogram import Bot, Dispatcher, types, executor


API_TOKEN = 'key'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        'Ты попал в капкан!'
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
