import random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='6298196236:AAEAjszNBfPbqr1BngEEIUhAfoNPFH86QCc')
dp = Dispatcher(bot)




@dp.message_handler(commands=['random_models'])
async def send_random_models(message: types.Message):
    random_models = random.sample(models, 3)
    for model in random_models:
        # Send the model's avatar
        await bot.send_photo(message.chat.id, open(model['avatar'], 'rb'))

        # Create an inline keyboard with a button for the model
        inline_keyboard = types.InlineKeyboardMarkup()
        inline_keyboard.add(types.InlineKeyboardButton(text="Show Photo", callback_data=model['photo']))

        # Send the inline keyboard
        await bot.send_message(message.chat.id, "🔻",
                               reply_markup=inline_keyboard)


@dp.callback_query_handler(lambda callback_query: True)
async def show_model_photo(callback_query: types.CallbackQuery):
    photo = callback_query.data

    # Send the model's photo
    await bot.send_photo(callback_query.message.chat.id, open(photo, 'rb'))
    await bot.send_message(callback_query.message.chat.id, "Please one moment🔎")



if __name__ == '__main__':
    executor.start_polling(dp)