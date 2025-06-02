from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#СТАРТОВАЯ КЛАВИАТУРА
start_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Далее', callback_data='example'),
     InlineKeyboardButton(text='Оплатить', callback_data='price')]
])

#Проходная клавиатура
example_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Понятно, дальше', callback_data='demonstration')]
])

#для подводки к покупке
price_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='А сколько стоит?', callback_data='price')]
])

#покупка
oplata_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Карта РФ', callback_data='oplata_rf'),
     InlineKeyboardButton(text='Stripe(в $)', callback_data='oplata_stripe')],
     [InlineKeyboardButton(text='Lava(в $)', callback_data='oplata_lava'),
      InlineKeyboardButton(text='Служба заботы', url='https://t.me/SQGED')]
])


############## ОПЛАТА #############

#ОПЛАТИТЬ рублем
pay_kb_ru = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Оплатить', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')]
])

#ОПЛАТИТЬ sprite
pay_kb_stripe = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Оплатить', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')]
])

#ОПЛАТИТЬ lava
pay_kb_lava = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Оплатить', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')]
])
