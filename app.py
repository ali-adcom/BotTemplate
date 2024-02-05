from aiogram import executor

from loader import dp
import filters

import handlers


async def on_startup(dp_):
    filters.setup(dp_)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)