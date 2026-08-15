import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


# ============================================================
# 🔑 ТОКЕН
# ============================================================

TOKEN = "...."


# ============================================================
# 🤖 BOT
# ============================================================

dp = Dispatcher()


# ============================================================
# 🎤 ОСНОВНАЯ ИНФОРМАЦИЯ
# ============================================================

INFO_TEXT = """
🎤 ADO — ИНФОРМАЦИЯ

🇯🇵 Имя: Ado
🎂 Дата рождения: 24 октября 2002 года
🎈 Возраст: 23 года
🇯🇵 Страна: Япония
🎙️ Дебют: 23 октября 2020 года
🎵 Дебютный сингл: Usseewa

━━━━━━━━━━━━━━━━━━
📖 ПУТЬ ADO
━━━━━━━━━━━━━━━━━━

Ado начала свой путь как utaite — исполнительница,
которая публиковала вокальные каверы в интернете.

Она начала выкладывать каверы ещё подростком,
а настоящий прорыв произошёл в 2020 году.

23 октября 2020 года, в возрасте 17 лет,
Ado официально дебютировала с песней «Usseewa».

Песня стала огромным хитом в Японии и достигла
№1 в Billboard Japan Hot 100 и Oricon.

«Usseewa» стала одной из самых узнаваемых песен
современной японской поп-культуры.

После этого появились:

• Readymade
• Gira Gira
• Odo
• Yoru no Pierrot
• Aitakute
• Ashura-chan

А в 2022 году вышел её первый студийный альбом
«Kyōgen».

━━━━━━━━━━━━━━━━━━
🏴‍☠️ ONE PIECE
━━━━━━━━━━━━━━━━━━

В 2022 году Ado стала вокальным голосом Уты
в фильме «One Piece Film: Red».

Она исполнила практически весь вокал персонажа Уты.

Главной песней стала «New Genesis».

Песни из фильма получили огромную популярность
как в Японии, так и за её пределами.

«New Genesis» возглавила мировой Top 100 Apple Music,
что стало историческим достижением для японской песни.

━━━━━━━━━━━━━━━━━━
💿 АЛЬБОМЫ
━━━━━━━━━━━━━━━━━━

2022 — Kyōgen
2022 — UTA'S SONGS ONE PIECE FILM RED
2023 — Ado's Utattemita Album
2024 — Zanmu
2025 — Ado's Best Adobum

━━━━━━━━━━━━━━━━━━
🌟 ИНТЕРЕСНЫЕ ФАКТЫ
━━━━━━━━━━━━━━━━━━

• Ado дебютировала в 17 лет.

• Она долгое время сохраняет анонимность
  и практически не показывает лицо публике.

• «Usseewa» стала №1 в Billboard Japan Hot 100.

• «Usseewa» достигла 100 миллионов стримов
  Billboard Japan всего за 17 недель.

• Ado стала самым молодым сольным исполнителем,
  достигшим этого результата.

• Ado исполнила вокал Уты в One Piece Film: Red.

• «New Genesis» стала первой японской песней,
  возглавившей глобальный чарт Apple Music Top 100.

• Ado работала с огромным количеством известных
  японских композиторов и продюсеров.

• Её вокальный стиль отличается большим количеством
  контрастов: от мягкого и чистого звучания
  до экстремально мощного и агрессивного вокала.

━━━━━━━━━━━━━━━━━━

Используй меню бота, чтобы узнать больше. 🎤
"""


# ============================================================
# 🎵 ОРИГИНАЛЬНЫЕ ПЕСНИ
# ============================================================

ORIGINAL_SONGS = [
    "Usseewa",
    "Readymade",
    "Gira Gira",
    "Odo",
    "Yoru no Pierrot",
    "Aitakute",
    "Ashura-chan",
    "Eien no Akuruhi",
    "New Genesis",
    "I'm Invincible",
    "Backlight",
    "Fleeting Lullaby",
    "Tot Musica",
    "Where the Wind Blows",
    "Rebellion",
    "I'm a Controversy",
    "Ibara",
    "Himawari",
    "Show",
    "Dignity",
    "Kura Kura",
    "All Night Radio",
    "Chocolat Cadabra",
    "Value",
    "Mirror",
    "RuLe",
    "Shoka",
    "Sakura Biyori and Time Machine",
    "Episode X",
    "Elf",
    "Bouquet for Me",
    "The Story of the Wind and I",
    "MAGIC",
    "Odoru Ponpokorin",
    "GeGeGe no Kitaro",
    "Stay Gold",
    "soldier game",
    "Angelseek",
    "Vivarium",
    "AiAiA",
    "KIRA",
    "Haru Ni Mau",
    "Love me forever!",
    "MONSTRUO"
]


# ============================================================
# 🎤 ОФИЦИАЛЬНЫЕ КАВЕРЫ
# ============================================================

COVERS = [
    "Aishite Aishite Aishite",
    "Crime and Punishment",
    "Darling Dance",
    "Unravel",
    "Villain",
    "Kokoronashi",
    "Love is War",
    "Missing",
    "Gimme x Gimme",
    "Fleeting Lullaby (Live / alternate performances)"
]


# ============================================================
# 🤝 КОЛЛАБОРАЦИИ
# ============================================================

COLLABS = [
    "Take Me to the Beach — Imagine Dragons feat. Ado",
    "UNFORGIVEN — LE SSERAFIM feat. Ado",
    "Stay Gold — Jax Jones & Ado",
    "Ready For My Show collaborations",
]


# ============================================================
# 🎬 ONE PIECE FILM: RED
# ============================================================

ONE_PIECE = [
    "New Genesis",
    "I'm Invincible",
    "Backlight",
    "Fleeting Lullaby",
    "Tot Musica",
    "The World's Continuation",
    "Where the Wind Blows"
]


# ============================================================
# 💿 АЛЬБОМЫ
# ============================================================

ALBUMS = {

    "Kyōgen": [
        "Usseewa",
        "Readymade",
        "Gira Gira",
        "Odo",
        "Yoru no Pierrot",
        "Aitakute",
        "Ashura-chan",
        "Eien no Akuruhi",
        "Motherland",
        "FREEDOM",
        "Kyōgen"
    ],

    "UTA'S SONGS ONE PIECE FILM RED": [
        "New Genesis",
        "I'm Invincible",
        "Backlight",
        "Fleeting Lullaby",
        "Tot Musica",
        "The World's Continuation",
        "Where the Wind Blows"
    ],

    "Ado's Utattemita Album": [
        "Aishite Aishite Aishite",
        "Crime and Punishment",
        "Darling Dance",
        "Unravel",
        "Villain",
        "Kokoronashi",
        "Love is War",
        "Missing",
        "Gimme x Gimme",
        "Other official cover selections"
    ],

    "Zanmu": [
        "RuLe",
        "Show",
        "Kura Kura",
        "All Night Radio",
        "Ibara",
        "Himawari",
        "Chocolat Cadabra",
        "Value",
        "Mirror",
        "Dignity",
        "Episode X",
        "Shoka",
        "Sakura Biyori and Time Machine"
    ],

    "Ado's Best Adobum": [
        "Usseewa",
        "Readymade",
        "Gira Gira",
        "Odo",
        "Yoru no Pierrot",
        "Aitakute",
        "Ashura-chan",
        "New Genesis",
        "Show",
        "Kura Kura",
        "Value",
        "RuLe",
        "Shoka",
        "Episode X",
        "Elf",
        "Bouquet for Me",
        "The Story of the Wind and I",
        "MAGIC",
        "AiAiA",
        "Vivarium",
        "Angelseek",
        "KIRA",
        "Haru Ni Mau",
        "Love me forever!",
        "MONSTRUO"
    ]
}


# ============================================================
# 🎛️ ГЛАВНОЕ МЕНЮ
# ============================================================

def main_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="🎤 Об Ado",
                    callback_data="info"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🎵 Песни",
                    callback_data="songs"
                ),

                InlineKeyboardButton(
                    text="💿 Альбомы",
                    callback_data="albums"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🌟 Факты",
                    callback_data="facts"
                )
            ]

        ]
    )


# ============================================================
# 🎵 МЕНЮ ПЕСЕН
# ============================================================

def songs_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="🎙️ Оригинальные",
                    callback_data="originals"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🎤 Каверы",
                    callback_data="covers"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🤝 Коллаборации",
                    callback_data="collabs"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🏴‍☠️ One Piece Film: Red",
                    callback_data="onepiece"
                )
            ],

            [
                InlineKeyboardButton(
                    text="⬅️ Назад",
                    callback_data="back"
                )
            ]

        ]
    )


# ============================================================
# 💿 МЕНЮ АЛЬБОМОВ
# ============================================================

def albums_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="🎭 Kyōgen",
                    callback_data="album_kyogen"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🏴‍☠️ UTA'S SONGS",
                    callback_data="album_uta"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🎤 Utattemita Album",
                    callback_data="album_uta_cover"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🌙 Zanmu",
                    callback_data="album_zanmu"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🏆 Ado's Best Adobum",
                    callback_data="album_best"
                )
            ],

            [
                InlineKeyboardButton(
                    text="⬅️ Назад",
                    callback_data="back"
                )
            ]

        ]
    )


# ============================================================
# 📃 СОЗДАНИЕ СПИСКА ПЕСЕН
# ============================================================

def make_song_list(title, songs):

    text = f"🎵 {title}\n\n"

    for number, song in enumerate(songs, 1):
        text += f"{number}. {song}\n"

    return text


# ============================================================
# 🚀 /START
# ============================================================

@dp.message(Command("start"))
async def start(message: Message):

    await message.answer(
        "🎤 Добро пожаловать в Ado Info Bot!\n\n"
        "Здесь ты можешь узнать больше об Ado, "
        "её пути, песнях, каверах и альбомах.\n\n"
        "Выбирай раздел ниже 👇",
        reply_markup=main_menu()
    )


# ============================================================
# ℹ️ /INFO
# ============================================================

@dp.message(Command("info"))
async def info_command(message: Message):

    await message.answer(
        INFO_TEXT,
        reply_markup=main_menu()
    )


# ============================================================
# 🎵 /SONGS
# ============================================================

@dp.message(Command("songs"))
async def songs_command(message: Message):

    await message.answer(
        "🎵 ПЕСНИ ADO\n\n"
        "Выбери нужную категорию:",
        reply_markup=songs_menu()
    )


# ============================================================
# 💿 /ALBUMS
# ============================================================

@dp.message(Command("albums"))
async def albums_command(message: Message):

    await message.answer(
        "💿 АЛЬБОМЫ ADO\n\n"
        "Выбери альбом:",
        reply_markup=albums_menu()
    )


# ============================================================
# 🌟 ФАКТЫ
# ============================================================

@dp.callback_query(F.data == "facts")
async def facts(callback: CallbackQuery):

    await callback.message.edit_text(
        "🌟 ИНТЕРЕСНЫЕ ФАКТЫ ОБ ADO\n\n"

        "🎂 Ado родилась 24 октября 2002 года.\n\n"

        "🎙️ Официально дебютировала 23 октября 2020 года "
        "с «Usseewa».\n\n"

        "🔥 «Usseewa» стала №1 в Billboard Japan Hot 100.\n\n"

        "🏆 Песня достигла 100 миллионов стримов "
        "Billboard Japan за 17 недель.\n\n"

        "🏴‍☠️ Ado стала вокальным голосом Уты "
        "в One Piece Film: Red.\n\n"

        "🌎 «New Genesis» возглавила мировой "
        "Top 100 Apple Music.\n\n"

        "🎭 Ado известна своей анонимностью "
        "и сильным акцентом на вокальном образе.\n\n"

        "🎤 Её песни создавались в сотрудничестве "
        "с большим количеством известных японских "
        "композиторов и продюсеров.",
        reply_markup=main_menu()
    )

    await callback.answer()


# ============================================================
# 🎤 ОБ ADO
# ============================================================

@dp.callback_query(F.data == "info")
async def info_button(callback: CallbackQuery):

    await callback.message.edit_text(
        INFO_TEXT,
        reply_markup=main_menu()
    )

    await callback.answer()


# ============================================================
# 🎵 ПЕСНИ
# ============================================================

@dp.callback_query(F.data == "songs")
async def songs_button(callback: CallbackQuery):

    await callback.message.edit_text(
        "🎵 ПЕСНИ ADO\n\n"
        "Выбери категорию:",
        reply_markup=songs_menu()
    )

    await callback.answer()


# ============================================================
# 🎙️ ОРИГИНАЛЬНЫЕ
# ============================================================

@dp.callback_query(F.data == "originals")
async def originals(callback: CallbackQuery):

    await callback.message.edit_text(
        make_song_list(
            "Оригинальные песни",
            ORIGINAL_SONGS
        ),
        reply_markup=songs_menu()
    )

    await callback.answer()


# ============================================================
# 🎤 КАВЕРЫ
# ============================================================

@dp.callback_query(F.data == "covers")
async def covers(callback: CallbackQuery):

    await callback.message.edit_text(
        make_song_list(
            "Официальные каверы",
            COVERS
        ),
        reply_markup=songs_menu()
    )

    await callback.answer()


# ============================================================
# 🤝 КОЛЛАБОРАЦИИ
# ============================================================

@dp.callback_query(F.data == "collabs")
async def collabs(callback: CallbackQuery):

    await callback.message.edit_text(
        make_song_list(
            "Коллаборации",
            COLLABS
        ),
        reply_markup=songs_menu()
    )

    await callback.answer()


# ============================================================
# 🏴‍☠️ ONE PIECE
# ============================================================

@dp.callback_query(F.data == "onepiece")
async def onepiece(callback: CallbackQuery):

    await callback.message.edit_text(
        make_song_list(
            "One Piece Film: Red",
            ONE_PIECE
        ),
        reply_markup=songs_menu()
    )

    await callback.answer()


# ============================================================
# 💿 АЛЬБОМЫ
# ============================================================

@dp.callback_query(F.data == "albums")
async def albums_button(callback: CallbackQuery):

    await callback.message.edit_text(
        "💿 АЛЬБОМЫ ADO\n\n"
        "Выбери альбом:",
        reply_markup=albums_menu()
    )

    await callback.answer()


# ============================================================
# 🎭 KYŌGEN
# ============================================================

@dp.callback_query(F.data == "album_kyogen")
async def album_kyogen(callback: CallbackQuery):

    await callback.message.edit_text(
        "🎭 KYŌGEN\n\n"
        "📅 26 января 2022 года\n"
        "💿 Дебютный студийный альбом Ado\n\n"
        + make_song_list(
            "Треклист",
            ALBUMS["Kyōgen"]
        ),
        reply_markup=albums_menu()
    )

    await callback.answer()


# ============================================================
# 🏴‍☠️ UTA
# ============================================================

@dp.callback_query(F.data == "album_uta")
async def album_uta(callback: CallbackQuery):

    await callback.message.edit_text(
        "🏴‍☠️ UTA'S SONGS ONE PIECE FILM RED\n\n"
        "📅 2022\n"
        "🎬 Музыка из One Piece Film: Red\n\n"
        + make_song_list(
            "Треклист",
            ALBUMS["UTA'S SONGS ONE PIECE FILM RED"]
        ),
        reply_markup=albums_menu()
    )

    await callback.answer()


# ============================================================
# 🎤 UTATTEMITA
# ============================================================

@dp.callback_query(F.data == "album_uta_cover")
async def album_uta_cover(callback: CallbackQuery):

    await callback.message.edit_text(
        "🎤 ADO'S UTATTEMITA ALBUM\n\n"
        "📅 2023\n"
        "🎙️ Альбом каверов\n\n"
        + make_song_list(
            "Треклист",
            ALBUMS["Ado's Utattemita Album"]
        ),
        reply_markup=albums_menu()
    )

    await callback.answer()


# ============================================================
# 🌙 ZANMU
# ============================================================

@dp.callback_query(F.data == "album_zanmu")
async def album_zanmu(callback: CallbackQuery):

    await callback.message.edit_text(
        "🌙 ZANMU\n\n"
        "📅 10 июля 2024 года\n"
        "💿 Второй студийный альбом Ado\n\n"
        + make_song_list(
            "Треклист",
            ALBUMS["Zanmu"]
        ),
        reply_markup=albums_menu()
    )

    await callback.answer()


# ============================================================
# 🏆 BEST ADOBUM
# ============================================================

@dp.callback_query(F.data == "album_best")
async def album_best(callback: CallbackQuery):

    await callback.message.edit_text(
        "🏆 ADO'S BEST ADOBUM\n\n"
        "📅 2025\n"
        "💿 Сборник лучших песен Ado\n\n"
        + make_song_list(
            "Треклист",
            ALBUMS["Ado's Best Adobum"]
        ),
        reply_markup=albums_menu()
    )

    await callback.answer()


# ============================================================
# ⬅️ НАЗАД
# ============================================================

@dp.callback_query(F.data == "back")
async def back(callback: CallbackQuery):

    await callback.message.edit_text(
        "🎤 ADO INFO BOT\n\n"
        "Выбери нужный раздел:",
        reply_markup=main_menu()
    )

    await callback.answer()


# ============================================================
# ▶️ ЗАПУСК
# ============================================================

async def main():

    bot = Bot(TOKEN)

    print("Ado Info Bot запущен!")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())	