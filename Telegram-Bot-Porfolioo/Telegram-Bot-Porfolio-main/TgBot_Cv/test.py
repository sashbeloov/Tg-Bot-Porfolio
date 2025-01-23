from aiogram import types, Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMedia, WebAppInfo
import asyncio

TOKEN = "7758945683:AAHMdKXctl6yDr1S6-4DM2zByqyBc6nTkbU"

bot = Bot(token=TOKEN)
dp = Dispatcher()
user_data = {}


@dp.message()
async def handle_text(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data or message.text == "/start":
        await start(message)
    elif "language" not in user_data[user_id]:
        await bosh_menu(message)
    elif message.text == "Bog'lanish 📞" or message.text == "/contact":
        await contact(message)
    elif message.text == "CV Yuklash 📥" or message.text == "/cv":
        await cv_download_menu(message)
    elif message.text == "Ortga ↙️" or message.text == "/menu":
        await bosh_menu(message)
    elif message.text == "Telegram 📨":
        await tginfo(message)
    elif message.text == "⬅️ ️Ortga":
        await contact(message)
    elif message.text == "Instagram 📸":
        await instainfo(message)
    elif message.text == "GitHub 💼":
        await githubinfo(message)
    elif message.text == "️Ortga":
        await contact(message)
    elif message.text == "Loyihalar 💻" or message.text == "/projects":
        await loyihalar(message)
    elif message.text == "Portfolio 📍":
        await portfolio(message)
    elif message.text == "Mening-sitelarim 🌐":
        await mysites(message)
    elif message.text == "️Ortga ↘️":
        await loyihalar(message)
    elif message.text == "Ta'lim 🧑‍🏫":
        await talim(message)
    elif message.text == "Kollej 🏫":
        await kollej(message)
    elif message.text == "Ortga ⬇️":
        await talim(message)
    elif message.text == "Kurslar 📚":
        await kurslar(message)
    elif message.text == "Ustudy 🧑‍💻":
        await ustudy(message)
    elif message.text == "Cambridge 🏴󠁧󠁢󠁥󠁮󠁧󠁿":
        await cambridge(message)
    elif message.text == "Supermiya 🧠👈":
        await supermiya(message)
    elif message.text == "Tajriba 🧑‍💻" or message.text == "/experience":
        await tajriba(message)
    elif message.text == "Korzinka 🛒":
        await korzinka(message)
    elif message.text == "SportMaster 🏀⚾️🎾":
        await sportmaster(message)
    elif message.text == "Havas 🛍️":
        await havas(message)





@dp.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    button = [
        [types.KeyboardButton(text="🇷🇺 Русский"), types.KeyboardButton(text="🇺🇿 O'zbekcha"),
         types.KeyboardButton(text="🇺🇸 English")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer(
        "Assalomu Alaykum! Ushbu bot yordamida siz Chayka Aleksandrning portfoliosi bilan tanishib chiqasiz.😊\n\n"
        "Здравствуйте! С помощью этого бота вы сможете ознакомиться с портфолио Чайка Александра.😊\n\n"
        "Hello! With this bot, you can explore Chayka Aleksandr's portfolio.😊",
        reply_markup=keyboard)
    print(1, user_data)


async def bosh_menu(message: types.Message):
    user_id = message.from_user.id
    language = message.text
    user_data[user_id]["language"] = "language"
    button = [
        [types.KeyboardButton(text="Loyihalar 💻"), types.KeyboardButton(text="Tajriba 🧑‍💻")],
        [types.KeyboardButton(text="Ta'lim 🧑‍🏫"), types.KeyboardButton(text="Bog'lanish 📞")],
        [types.KeyboardButton(text="CV Yuklash 📥")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer(
        "Quyidagi tugmalardan birini tanlang:\n\n"
        "💻 Loyihalar — Mening loyihalarim bilan tanishing.\n\n"
        "🧑‍💻 Tajriba — Tajribam haqida ma'lumot oling.\n\n"
        "🧑‍🏫 Ta'lim— Rezyumeni yuklab olish.\n\n"
        "📞 Bog'lanish — Mening aloqalarimni ko‘rish.\n\n"
        "📥 CV Yuklash — Rezyumeni yuklab olish.\n\n👇👇👇👇",
        reply_markup=keyboard
    )
    print(2, user_data)

# rasm joylash diskni o'zidan
async def cv_download_menu(message: types.Message):
    user_id = message.from_user.id
    button = [
        [types.KeyboardButton(text="Ortga ↙️")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    file_path = "../images/CV-resume.jpg"
    await message.reply_photo(photo=types.FSInputFile(path=file_path,))
    await message.answer("Bu mening rezyumem. Yuklab oling! 😊", reply_markup=keyboard)
    print("CV yuborildi!")
    # C:\Users\Windows10\Desktop\TgBot_Cv\images


async def contact(message: types.Message):
    user_id = message.from_user.id
    button = [
        [types.KeyboardButton(text="Telegram 📨"), types.KeyboardButton(text="Instagram 📸")],
        [types.KeyboardButton(text="Ortga ↙️")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Men bilan quyidagi platformalar orqali bog‘lanishingiz mumkin. Tugmalardan birini tanlang:\n👇👇👇👇",reply_markup=keyboard)




async def tginfo(message: types.Message):
    user_id = message.from_user.id
    button = [
        [types.KeyboardButton(text="⬅️ ️Ortga")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Men bilan bog'lanish uchun kontaktlar: \n\nhttps://t.me/Belovsasha ✉️ \n\nTelefon raqam: +998-33-545-05-42 ☎️",reply_markup=keyboard)
    print('tg', user_data)




async def instainfo(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "instainfo"
    buttons = [
        [types.InlineKeyboardButton(text="Instagramga havola",url="https://www.instagram.com/sashbeloov?igsh=MXNidW1nMGZ2ZWh2dw%3D%3D&utm_source=qr"),],
    ]
    file_path = "../images/instagram.jpg"
    await message.reply_photo(photo=types.FSInputFile(path=file_path, ))
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True)
    await message.answer("Instagram uchun havolani ustiga bosing: \n👇👇👇👇",reply_markup=keyboard)


async def loyihalar(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "loyihalar"
    button = [
        [types.KeyboardButton(text="Portfolio 📍")],
        [types.KeyboardButton(text="Mening-sitelarim 🌐"),types.KeyboardButton(text="GitHub 💼")],
        [types.KeyboardButton(text="Ortga ↙️")],
    ]
    file_path = "../images/myprojects.jpg"
    await message.reply_photo(photo=types.FSInputFile(path=file_path, ))
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Bu yerda siz menig Loyihalarim bilan tanishib chiqasiz 🧑‍💻\n",reply_markup=keyboard)


async def githubinfo(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "githubinfo"
    button = [
        [types.InlineKeyboardButton(text="GitHubga havola",
                                    url="https://github.com/sashbeloov?tab=repositories")]
    ]
    file_path = "../images/GitHub-logo.png"
    await message.reply_photo(photo=types.FSInputFile(path=file_path, ))
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    await message.answer("GitHub orqali siz mening loyihalarimning kodlari bilan tanishib chiqishingiz mumkin 🗂\n\nGitHub uchun havolani ustiga bosing: \n👇👇👇👇",reply_markup=keyboard)



async def portfolio(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "portfolio"
    button = [
        [types.InlineKeyboardButton(text='Websiteni ochish',url="https://t.me/Aleksandr_Portfolioo_bot/Portfolio")]
    ]
    file_path = "../images/website.png"
    await message.reply_photo(photo=types.FSInputFile(path=file_path, ))
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    await message.answer("Bu tugmani bosish orqali siz mening portfolio websiteimga kirasiz 👇👇👇👇",reply_markup=keyboard)


async def mysites(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "mysites"
    button = [
        [types.InlineKeyboardButton(text='Youtube klone', url="https://youtube-cloneuz.netlify.app/"),
         types.InlineKeyboardButton(text='Traveluz', url="https://sayohat-uz.netlify.app/")],
        [types.InlineKeyboardButton(text='Shoesuz', url="https://shoes-uz.netlify.app/"),
         types.InlineKeyboardButton(text='Fast-Food-Uz', url="https://fast-food-uz.netlify.app/")],
        [types.InlineKeyboardButton(text='Parralax-website', url="https://parralax-websitee.netlify.app/"),
         types.InlineKeyboardButton(text='Soat-uz', url="https://soat-uzz.netlify.app/")],
    ]
    file_path = "../images/websitee.jpg"
    await message.reply_photo(photo=types.FSInputFile(path=file_path, ))
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    await message.answer("Mening sitelarimni ko'rish uchun pastda turgan tugmalarni bosing \n👇👇👇👇👇👇",reply_markup=keyboard)


async def talim(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "talim"
    button = [
        [types.KeyboardButton(text="Kurslar 📚"),types.KeyboardButton(text="Kollej 🏫")],
        [types.KeyboardButton(text="Ortga ↙️")],
    ]
    file_path = "../images/education.jpg"
    await message.reply_photo(photo=types.FSInputFile(path=file_path, ))
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Bu yerda siz mening qaysi kollejni o'qiganim va qaysi kurslarni bitirganim haqida to'liq ma'lumot olasiz. 🧑‍💻\nBuning uchun pastdagi tugmalarni ustiga bosing:\n👇👇👇👇👇👇",reply_markup=keyboard)


async def kollej(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["kollej"] = "kollej"
    await message.answer("Toshkent Iqtisodiyot Kolleji 🏫\n\nBuxgalteriya hisobi va audit yo'nalishi \n\n2015 – 2018 🗓"
                         "\n\nToshkent Iqtisodiyot Kollejida buxgalteriya hisobi va audit yo'nalishi bo'yicha ta'lim oldim. O'qish davomida buxgalteriya hisobi, moliyaviy tahlil, soliq qonunchiligi va audit metodologiyasi kabi sohalarda chuqur bilimlarga ega bo'ldim. Ushbu yo'nalish bo'yicha amaliyotlar orqali real ish sharoitlarida tejamkor va to'g'ri hisob-kitoblarni amalga oshirish ko'nikmalarini rivojlantirdim. 😊")


async def kurslar(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "kurslar"
    button = [
        [types.KeyboardButton(text="Ustudy 🧑‍💻")],
        [types.KeyboardButton(text="Cambridge 🏴󠁧󠁢󠁥󠁮󠁧󠁿"),types.KeyboardButton(text="Supermiya 🧠👈")],
        [types.KeyboardButton(text="Ortga ⬇️")],
    ]
    file_path = "../images/education.jpg"
    await message.reply_photo(photo=types.FSInputFile(path=file_path, ))
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Men o'qigan kurslarim haqida batafsil malunmotlar 📚",reply_markup=keyboard)



async def ustudy(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "Ustudy"
    file_path = "../images/ustudy.jpeg"
    await message.reply_photo(photo=types.FSInputFile(path=file_path, ))
    await message.answer("Ustudy: Pythonai \n\n"
                         "2024-2025 📆\n\n"
                         "Ustudy o‘quv markazida Python dasturlash tilini, data analysis va sun’iy intellekt yo‘nalishlarini tahsil olganman. Kurs amaliyotga yo‘naltirilgan va real loyihalar ustida ishlashga yordam berdi. 💻")


async def cambridge(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "cambridge"
    file_path = "../images/images.jpg"
    await message.reply_photo(photo=types.FSInputFile(path=file_path, ))
    await message.answer("Cambridge \n\n"
                         "2021-2022 📆\n\n"
                         "Cambridge markazida ingliz tilining turli darajalari bo‘yicha chuqur bilimlarga ega bo‘ldim, jumladan Elementary, Pre-Intermediate va Intermediate bosqichlarini muvaffaqiyatli tugatdim. 🏴󠁧󠁢󠁥󠁮󠁧󠁿")


async def supermiya(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "cambridge"
    file_path = "../images/supermiya.jpg"
    await message.reply_photo(photo=types.FSInputFile(path=file_path, ))
    await message.answer("Supermiya \n\n"
                         "2023 📆\n\n"
                         "Supermiya o‘quv markazida mnemotexnika va intellektual ko‘nikmalarni rivojlantirish bo‘yicha kurslarda tahsil oldim. 🧠👈")



async def tajriba(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "tajriba"
    button = [
        [types.KeyboardButton(text="Korzinka 🛒")],
        [types.KeyboardButton(text="SportMaster 🏀⚾️🎾"), types.KeyboardButton(text="Havas 🛍️")],
        [types.KeyboardButton(text="Ortga ↙️")],
    ]
    file_path = "../images/experience.jpg"
    await message.reply_photo(photo=types.FSInputFile(path=file_path, ))
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Bu bo'limda siz mening tajribam haqida ma'lumot olasiz. 🗂\n\n"
                         "Tugmalar ustiga bosing va batafsil ma'lumot oling. \n👇👇👇👇👇👇",reply_markup=keyboard)



async def korzinka(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "korzinka"
    file_path = "../images/korzinka.jpg"
    await message.reply_photo(photo=types.FSInputFile(path=file_path, ))
    await message.answer("Korzinka \n\n"
                         "2020-2024 🗓\n\n"
                         "Lavozim: Bosh Kassir va Kassir nazoratchi.\n\n"
                         "Korzinka tarmog‘ida ishlash faoliyatim oddiy kassir sifatida boshlaganman. Ish jarayonida savdo tizimlari, mijozlarga xizmat ko‘rsatish va ish samaradorligini oshirish bo‘yicha ko‘p tajriba orttirdim. Bu menga kassir nazoratchi va katta nazoratchi darajasiga ko‘tarilish imkonini berdi. 🌟")


async def sportmaster(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "sportmaster"
    file_path = "../images/sportmaster.png"
    await message.reply_photo(photo=types.FSInputFile(path=file_path, ))
    await message.answer("SportMaster \n\n"
                         "2024 🗓\n\n"
                         "Lavozim: Bosh Kassir.\n\n"
                         "Men Sportmaster do‘konida bosh kassir lavozimida faoliyat yuritdim. Bu davrda mijozlarga xizmat ko‘rsatish sifati va kassirlar jamoasining ish jarayonlarini samarali tashkil qilish bo‘yicha tajriba orttirdim. Bosh kassir sifatida savdo operatsiyalarini nazorat qilish va jamoani boshqarishda mas’uliyatli vazifalarni muvaffaqiyatli bajardim. 🏀🎾⚾️")


async def havas(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "havas"
    file_path = "../images/havas.png"
    await message.reply_photo(photo=types.FSInputFile(path=file_path, ))
    await message.answer("Havas Food \n\n"
                         "2020 🗓\n\n"
                         "Lavozim: Sotuvchi-kassir.\n\n"
                         "Men Havas do‘konida sotuvchi-kassir lavozimida ishladim. Ushbu lavozimda mijozlarga xizmat ko‘rsatish, savdo jarayonlarini boshqarish va kassa amaliyotlarini bajarish bo‘yicha tajriba orttirdim. ✨")



async def main():
    print('The bot is running...')
    await dp.start_polling(bot)


asyncio.run(main())




