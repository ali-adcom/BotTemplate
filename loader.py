from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN

# Create bot
bot = Bot(BOT_TOKEN, parse_mode=types.ParseMode.HTML)

# Create Storage
storage = MemoryStorage()

# Create dispatcher
dp = Dispatcher(bot, storage=storage)