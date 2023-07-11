import asyncio  # Работа с асинхронностью

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command  # Фильтр для /start, /...
from aiogram.types import Message  # Тип сообщения

from config import config  # Config
import AI

API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()  # Менеджер бота


# dp.message - обработка сообщений
# Command(commands=['start'] Фильтр для сообщений, берём только /start
@dp.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer("Привет!")


@dp.message(F.photo)
async def do_answer(message: Message):
    answer = AI.generate_answer()
    if answer:
        await message.answer(answer)


async def main():
    try:
        print('Bot Started')
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':  # Если мы запускаем конкретно этот файл.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
