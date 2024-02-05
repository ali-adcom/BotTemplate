from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import BoundFilter


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        return True


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsAdmin)