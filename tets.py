from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
from search import Search
from getlink import Getlink
import requests
from bs4 import BeautifulSoup
from stuff import Stuff

bot = Bot(token='6298196236:AAEAjszNBfPbqr1BngEEIUhAfoNPFH86QCc')

dp = Dispatcher(bot)



dp.message_handler(commands="start")
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("Top👑Models")
    button2 = KeyboardButton("Hot🔥Models")
    button3 = KeyboardButton("FastLink💨")
    keyboard.add(button1, button2, button3)
    user_name = message.from_user.first_name
    await message.answer(f"Hello, {user_name}!\nIt is free 💙Onlyfans💙 where you can search models by @name and get photos-videos\n"
                         f"First make sure you are member in our channel💙 OnflyfansFreee 💙"
                         f" Then you can write model name by adding @ before name!",reply_markup=keyboard)
@dp.message_handler(Text(equals="Top👑Models"))
async def get_hot(message: types.Message):

    top_list = ['@emarrb','@yoloschnitzelx','@hannahowo','@chocoletmilkk','@corinnakopf','@ellebrookeuk','@bunni.emmie','@realskybri','@soogsx','@megnut','@whoahannahjo','@hot4lexi']
    for model in top_list:

        word = model.find("@")
        search_word = model[word + 1:].lower()
        with open(f'avatar/{search_word}.jpg', "rb") as photo_file:
            await bot.send_photo(chat_id=message.chat.id, photo=photo_file, caption=model)
            inline_keyboard = types.InlineKeyboardMarkup()
            inline_keyboard.add(types.InlineKeyboardButton(text="Photo", callback_data=model))
            inline_keyboard.add(types.InlineKeyboardButton(text="Video", callback_data=f"https://hotleak.vip/{search_word}"))
            # Send the inline keyboard
            await bot.send_message(message.chat.id, "🔻",
                                   reply_markup=inline_keyboard)

    await message.answer(f"You can copy @name  and send it to me 💙")

@dp.callback_query_handler(lambda callback_query: True)
async def show_model_photo(callback_query: types.CallbackQuery):
    answer = callback_query.data
    if "@" in answer:

        user_message = answer
        word = user_message.find("@")
        search_word = user_message[word + 1:].lower()
        call = Search(search_word)
        answer = call.search()

        if len(answer) == 1:
            await bot.send_message(callback_query.message.chat.id, "Please one moment🔎")
            if call.look():
                link = call.send_link()
                url = f'https://hotleak.vip/{answer[0]}'
                response = requests.get(url=url).text

                soup = BeautifulSoup(response, "lxml")

                image_num = soup.find(id="photos-tab").text
                video_num = soup.find(id="videos-tab").text
                await bot.send_message(callback_query.message.chat.id, f"Model's gallery contains {image_num} and {video_num},\n"
                                     f"Here you see part of it💙")
                await bot.send_message(callback_query.message.chat.id, link)

            else:
                await bot.send_message(callback_query.message.chat.id, "It will take 10-30 seconds⏳💙")

                download = Getlink(f'https://hotleak.vip/{answer[0]}')
                download.one_step()
                link = call.send_link()
                url = f'https://hotleak.vip/{answer[0]}'
                response = requests.get(url=url).text

                soup = BeautifulSoup(response, "lxml")

                image_num = soup.find(id="photos-tab").text
                video_num = soup.find(id="videos-tab").text
                await bot.send_message(callback_query.message.chat.id, f"Model's gallery contains {image_num} and {video_num},\n"
                                     f"Here you see part of it💙")
                await bot.send_message(callback_query.message.chat.id, link)
    else:
        await bot.send_message(callback_query.message.chat.id,"I should send video")



def main():
    executor.start_polling(dp)


if __name__=='__main__':
    main()
