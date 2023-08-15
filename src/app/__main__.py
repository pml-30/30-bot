import asyncio
import logging

from aiogram import Bot, Dispatcher
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.app.core.config import ApplicationSettings

logger = logging.getLogger("app")


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)-8s [%(asctime)s] :: %(name)s : %(message)s"
    )

    settings = ApplicationSettings()

    bot = Bot(settings.bot.token.get_secret_value())
    dp = Dispatcher()

    db_engine = create_async_engine(str(settings.database.dsn))
    session_pool = async_sessionmaker(db_engine, expire_on_commit=False)

    try:
        logger.warning("Starting application")
        await dp.start_polling(bot)
    finally:
        await dp.storage.close()
        await db_engine.dispose()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.warning("Application stopped")
