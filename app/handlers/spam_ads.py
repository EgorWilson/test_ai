from aiogram import Bot, Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
import asyncio
import os

from app.keyboards import oplata_kb

router = Router()


async def send_delayed_advertisement(bot: Bot, chat_id: int):
    await asyncio.sleep(10)  # Ждем 10 секунд
    photo_path = os.path.join("image", "price_photo.jpg")
    await bot.send_photo(
        chat_id=chat_id,
        photo=FSInputFile(photo_path),
        caption=(
            "Ладно, вот в 4 раза дешевле.\n\n"
            "329Р за пробный период!\n\n"
            "И за это ты получаешь:\n"
            "✔️ 10 фотографий\n✔️ 100 стилей на выбор\n"
            "✔️ 1 модель аватара\n✔️ Канал с 5.000 идей фото"
        ),
        reply_markup=oplata_kb,
        parse_mode="Markdown"
    )
