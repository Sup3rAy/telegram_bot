from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
from search import Search
from getlink import Getlink
import requests
from bs4 import BeautifulSoup
from stuff import Stuff

#add your telegram ot token here.
bot = Bot(token=-)

dp = Dispatcher(bot)



@dp.message_handler(commands="start")
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
    channel_id = -1001877342402
    user_id = message.from_user.id

    chat_member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)

    if chat_member.status == 'member' or 1 == 1:
        top_list = ['@emarrb','@yoloschnitzelx','@hannahowo','@chocoletmilkk','@corinnakopf','@ellebrookeuk','@bunni.emmie','@realskybri','@soogsx','@megnut','@whoahannahjo','@hot4lexi']
        for model in top_list:
            button = InlineKeyboardButton(text="Photos", callback_data="Videos")
            keyboard_inline = InlineKeyboardMarkup().add(button)
            word = model.find("@")
            search_word = model[word + 1:].lower()
            with open(f'avatar/{search_word}.jpg', "rb") as photo_file:
                await bot.send_photo(chat_id=message.chat.id, photo=photo_file, caption=model)
                await message.reply(reply_markup=keyboard_inline)

        await message.answer(f"You can copy @name  and send it to me 💙")
    else:
        await message.reply('You are not subscribed to the channel.\nPlease subscribed to the channel.\nhttps://t.me/OnlyfansFree_chanel')

@dp.message_handler(Text(equals="Hot🔥Models"))
async def get_hot(message: types.Message):
    channel_id = -1001877342402
    user_id = message.from_user.id

    chat_member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)

    if chat_member.status == 'member' or 1 == 1:
        hot = Stuff()
        hot_models = hot.hot_models()

        for model in hot_models:
            word = model.find("@")
            search_word = model[word + 1:].lower()
            with open(f'avatar/{search_word}.jpg', "rb") as photo_file:
                await bot.send_photo(chat_id=message.chat.id, photo=photo_file, caption=model)

        await message.answer(f"You can copy @name  and send it to me 💙")
    else:
        await message.reply('You are not subscribed to the channel.\nPlease subscribed to the channel.\nhttps://t.me/OnlyfansFree_chanel')

@dp.message_handler(Text(equals="FastLink💨"))
async def get_hot(message: types.Message):
    channel_id = -1001877342402
    user_id = message.from_user.id

    chat_member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)

    if chat_member.status == 'member' or 1 == 1:
        rand = Stuff()
        links = rand.random_link()

        for link in links:
            await message.answer(link)
    else:
        await message.reply('You are not subscribed to the channel.\nPlease subscribed to the channel.\nhttps://t.me/OnlyfansFree_chanel')







@dp.message_handler()
async def get_model(message: types.Message):
    channel_id = -1001877342402
    user_id = message.from_user.id

    chat_member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)

    if chat_member.status == 'member' or 1 == 1:
        if '@' in message.text:

            user_message = message.text
            word = user_message.find("@")
            search_word = user_message[word + 1:].lower()
            call = Search(search_word)
            answer = call.search()

            if len(answer) == 1:
                await message.answer("Please one moment🔎")
                if call.look():
                    link = call.send_link()
                    url = f'https://hotleak.vip/{answer[0]}'
                    response = requests.get(url=url).text

                    soup = BeautifulSoup(response, "lxml")

                    image_num = soup.find(id="photos-tab").text
                    video_num = soup.find(id="videos-tab").text
                    await message.answer(f"Model's gallery contains {image_num} and {video_num},\n"
                                         f"Here you see part of it💙")
                    await message.answer(link)
                else:
                    await message.answer("It will take 10-30 seconds⏳💙")
                    download = Getlink(f'https://hotleak.vip/{answer[0]}')
                    download.one_step()
                    link = call.send_link()
                    url = f'https://hotleak.vip/{answer[0]}'
                    response = requests.get(url=url).text

                    soup = BeautifulSoup(response, "lxml")

                    image_num = soup.find(id="photos-tab").text
                    video_num = soup.find(id="videos-tab").text
                    await message.answer(f"Model's gallery contains {image_num} and {video_num},\n"
                                         f"Here you see part of it💙")
                    await message.answer(link)


            elif len(answer) == 0:
                await message.answer("Sorry we don't find model🤕")


            else:
                if len(answer) > 15:
                    await message.answer(f"There is more than 15 models similar to this name💙..\n"
                                         f"Enter full name or select one of the following ")
                    for i in range(15):
                        # await message.answer(f"You meant @{answer[i]}")
                        with open(f'avatar/{answer[i]}.jpg', "rb") as photo_file:
                            await bot.send_photo(chat_id=message.chat.id, photo=photo_file, caption=f"@{answer[i]}")
                        # await bot.send_photo(chat_id=message.chat.id, photo=open(f'avatar/{answer[i]}.jpg', 'rb',caption=f"@{answer[i]}"))
                    await message.answer(f"You can copy @name  and send it back💙")
                else:
                    for st in answer:
                        with open(f'avatar/{st}.jpg', "rb") as photo_file:
                            await bot.send_photo(chat_id=message.chat.id, photo=photo_file, caption=f"@{st}")
                    await message.answer(f"You can copy @name  and send it back💙")
                    # await bot.send_photo(chat_id=message.chat.id, photo=open(f'avatar/{st}.jpg', 'rb',caption=f"@{st}"))
                    # await message.answer(f"You meant @{st}")

        else:
            await message.answer(f"You can search for model by adding '@' before model's name \n"
                                 f"for example copy @yoloschnitzelx send it to me🔎 ")
    else:
        await message.reply('You are not subscribed to the channel.\nPlease subscribed to the channel.\nhttps://t.me/OnlyfansFree_chanel')



def main():
    executor.start_polling(dp)


if __name__=='__main__':
    main()
