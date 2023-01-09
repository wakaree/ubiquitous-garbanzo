
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

import config

# Настраиваем логгирование
logging.basicConfig(handlers=(logging.FileHandler('logs.txt', encoding='utf-8'), logging.StreamHandler()),
                    format='[%(asctime)s] %(levelname)s | %(name)s.%(module)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

# Подключаемся к боту
bot = Bot(token=config.API_TOKEN, parse_mode='html')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    name_input = State()  # Состояние, в котором ожидается ввод пользователем своего имени


# Выполняется при запуске приложения
async def startup_func(_):
    logging.info("Glückliches neues Jahr!")


@dp.message_handler(commands=['start', 'welcome'])
async def start_commands(message: types.Message):
    await message.answer(f"👋 <b>Привет, <a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a></b>")
    await message.answer(f"❓ <b>Могу ли я узнать Ваше имя?</b>")
    await UserState.name_input.set()


@dp.message_handler(state=UserState.name_input)
async def getusername(message: types.Message, state: FSMContext):
    await message.answer(f"🥂 <b> С Новым годом, <a href='tg://user?id={message.from_user.id}'>{message.text.title()}</a>!</b>")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=startup_func)
