import os
from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import FSInputFile

from data.database import add_user

from app.keyboards import *

router = Router()

#Приветствие
@router.message(Command('start'))
async def start(message: types.Message):
    add_user(message.from_user.id)

    photo_start = os.path.join("image", "startovaia.jpg")
    await message.answer_photo(
        photo=FSInputFile(photo_start),
        caption='Привет! Давай знакомиться 😊\n'
                'Мы — Вова, Артур и Олег, создатели Чиз.\n'
                '🧀 ЧИЗ ИИ — это нейросеть, которая создаёт крутые фото с вашим лицом, '
                'отражает лучшие черты и раскрывает творческий потенциал!\n\n'
                '💡 Раз уж вы здесь по рекомендации, расскажем, как это работает!',
        reply_markup=start_kb,
        parse_mode="Markdown"
    )

#Примеры работ
@router.callback_query(F.data == 'example')
async def callback_example(callback_query: types.CallbackQuery):
    photo_example = os.path.join("image", "example.jpg")

    await callback_query.message.answer_photo(
        photo=FSInputFile(photo_example),
        caption='🔥 Вот примеры того, что каждый день делает ЧИЗ ИИ!\n\n'
                'Это работы обычных пользователей из чата.\n\n'
                '📸 Просто загружаешь несколько своих фото из фотопленки, '
                'ИИ обучается твоему аватару и затем рождаются фантастические образы с тобой!',
        reply_markup=example_kb,
        parse_mode="Markdown"
    )
    await callback_query.answer()


#Демоснтрация популярности
@router.callback_query(F.data == 'demonstration')
async def callback_example(callback_query: types.CallbackQuery):
    photo_demonstration = os.path.join("image", "demonstration.jpg")

    await callback_query.message.answer_photo(
        photo=FSInputFile(photo_demonstration),
        caption='🌟 Уже более 1 000 000 человек попробовали ЧИЗ ИИ! Теперь ваша очередь!\n\n'
                '🎭🧞‍♂️ Два режима на выбор:\n'
                '1️⃣ Готовые идеи — 100+ стилей: от богемных образов до рок-звезды!\n'
                '2️⃣ Режим Бога — просто опишите желаемый образ или скидываешь фото референс,'
                ' а ИИ создаст уникальную фотографию!\n\n'
                '✨ Теперь к волшебству. Так как вы пришли по рекомендации, для вас специальные условия!',
        reply_markup=price_kb,
        parse_mode="Markdown"
    )
    await callback_query.answer()

#Цена и режимы работ
@router.callback_query(F.data == 'price')
async def callback_example(callback_query: types.CallbackQuery):
    photo_price = os.path.join("image", "price_photo.jpg")

    await callback_query.message.answer_photo(
        photo=FSInputFile(photo_price),
        caption='💥 Скидка 73%!\n\n'
                '💰 1390₽ вместо 5150₽\n\n'
                '📦 В пакет входит:\n✅ 90 фотографий\n✅ 100 стилей на выбор'
                '✅ 1 модель аватара\n✅ Режим Бога\n✅ Канал с 5.000 идей\n💬 Чат с участниками\n\n'
                '⏳ Бонус! При оплате в течение 30 минут — дополнительно 10 генераций в подарок! 🎁',
        reply_markup=oplata_kb,
        parse_mode="Markdown"
    )

    await callback_query.answer()


#ОПЛАТА В РУБЛЯХ
@router.callback_query(F.data == 'oplata_rf')
async def message_oplata_rf(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Оплата в российских рублях 🇷🇺\n\n'
                         '🔁 Оплатить можно только картой банка РФ.\n\n'
                         '👇 Нажмите кнопку ниже, чтобы произвести оплату 👇', reply_markup=pay_kb_ru)
    await callback_query.answer()

#ОПЛАТА В ДОЛЛАРАХ США(USD)
@router.callback_query(F.data == 'oplata_stripe')
async def message_oplata_rf(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Оплата в долларах США (USD) 🇺🇸\n\n'
                         '🔁🔁 Не волнуйтесь, если валюта вашей карты отличается - '
                                        'банк автоматически конвертирует сумму.\n\n'
                         '👇 Нажмите кнопку ниже, чтобы произвести оплату 👇', reply_markup=pay_kb_stripe)
    await callback_query.answer()


#ОПЛАТА В Lava (в $)
@router.callback_query(F.data == 'oplata_lava')
async def message_oplata_rf(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Укажите, пожалуйста, ваш email\n\n'
                                        '(этого просит платежная система)', reply_markup=pay_kb_lava)
    await callback_query.answer()