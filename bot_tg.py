import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработка команды /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Добро пожаловать, я Arion")

# Обработа команды /help
@dp.message(Command("help"))
async def help(message: types.Message):
    await message.answer("Список моих функций: \n /start - приветствие \n /help - меню с командами")
# обработка любого другого смс пользователя
@dp.message()
async def f(message: types.Message):
    await message.answer("Пока я не умею ничего делать, но в скором времени я смогу помочь тебе!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())