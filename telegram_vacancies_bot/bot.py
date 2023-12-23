from aiogram import Bot, Dispatcher, executor
from config import API_TOKEN
from database.database import Database
from handlers.hr_handlers import register_hr_handlers
# from handlers.job_seeker_handlers import register_job_seeker_handlers
from handlers.common_handlers import register_common_handlers
from aiogram.contrib.fsm_storage.memory import MemoryStorage


def main():
    storage = MemoryStorage()
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot, storage=storage)

    database = Database()

    # Register handlers
    register_common_handlers(dp, bot, database)
    register_hr_handlers(dp, bot, database)
    # register_job_seeker_handlers(dp, bot, database)

    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
