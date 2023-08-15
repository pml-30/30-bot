import asyncio
import logging

from aiogram import Bot, Dispatcher
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

logger = logging.getLogger("app")


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)-8s [%(asctime)s] :: %(name)s : %(message)s"
    )

    bot = Bot(...)
    dp = Dispatcher()

    db_engine = create_async_engine(...)
    session_pool = async_sessionmaker(db_engine, expire_on_commit=False)

    try:
        logger.warning("Starting application")
        await dp.start_polling(bot)
    finally:
        await dp.storage.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.warning("Application stopped")
