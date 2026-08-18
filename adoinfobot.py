import asyncio
import os
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

TOKEN = os.getenv("BOT_TOKEN")



# ============================================================
# 🤖 BOT
# ============================================================

dp = Dispatcher()


# ============================================================
# 🎤 ОСНОВНАЯ ИНФОРМАЦИЯ
# ============================================================


# ============================================================
# 🎤 ОБ ADO — ОСНОВНАЯ ИНФОРМАЦИЯ
# ============================================================

INFO_TEXT = """
🎤 ADO

Ado — японская певица и utaite, известная мощной и
разнообразной манерой исполнения и сохраняющейся
анонимностью публичного образа.

🎂 Дата рождения: 24 октября 2002 года
🇯🇵 Страна: Япония
🎙️ Мейджор-дебют: 23 октября 2020 года
🎵 Дебютная песня: «Usseewa»

Ado начала публиковать «歌ってみた» — вокальные каверы —
в интернете ещё до мейджор-дебюта. В 2020 году она
дебютировала с «Usseewa», после чего её карьера быстро
вышла за пределы интернет-сцены.

Используй подразделы ниже, чтобы отдельно посмотреть
биографию, хронологию, достижения, музыкальный путь
и основные проекты Ado.
"""


ABOUT_SECTIONS = {
    "bio": """
📖 БИОГРАФИЯ ADO

Ado родилась 24 октября 2002 года в Японии.

С юности она интересовалась интернет-культурой,
Vocaloid и исполнителями utaite. До профессионального
дебюта Ado публиковала вокальные каверы в интернете.

23 октября 2020 года Ado официально дебютировала
на мейджор-лейбле с песней «Usseewa».

В 2022 году вышел её первый оригинальный студийный
альбом «Kyōgen».

В 2024 году Ado выпустила второй оригинальный альбом
«Zanmu», провела мировой тур «Wish» и выступила
на Национальном стадионе в рамках Ado SPECIAL LIVE
2024 «Shinzou».

В 2025 году вышел первый сборник лучших песен
«Ado's Best Adobum», после чего состоялся мировой
тур «Hibana» и японский купольный тур «Yodaka».

В 2026 году Ado продолжила выпускать новые песни
и провела Ado STADIUM LIVE 2026 «Ao».
""",

    "timeline": """
📅 ХРОНОЛОГИЯ

2017
• Начала публиковать вокальные каверы в интернете.

2020
• 23 октября — мейджор-дебют с «Usseewa».

2021
• Выпускает «Gira Gira», «Odo», «Yoru no Pierrot»
  и другие песни, укрепляя популярность.

2022
• 26 января — первый студийный альбом «Kyōgen».
• Исполняет вокал Уты в «ONE PIECE FILM RED».
• Выходит «Uta's Songs: ONE PIECE FILM RED».

2023
• 13 декабря — «Ado's Utattemita Album».

2024
• Мировой тур Ado THE FIRST WORLD TOUR «Wish».
• 27–28 апреля — Ado SPECIAL LIVE 2024 «Shinzou»
  на Национальном стадионе.
• 10 июля — второй оригинальный альбом «Zanmu».
• 24 октября — первый CD-сингл
  «Sakura Biyori and Time Machine with Hatsune Miku /
  Shoka».

2025
• 9 апреля — первый best album «Ado's Best Adobum».
• Мировой тур Ado WORLD TOUR 2025 «Hibana».
• «Stay Gold» с Jax Jones.
• «CAT'S EYE» и «MAGIC» для новой версии
  «Cat's Eye».
• «GeGeGe no Kitaro».
• «Odoru Ponpokorin».

2026
• «Angelseek», «Vivarium», «AiAiA», «KIRA»,
  «Haru Ni Mau», «Love me forever!».
• 4–5 июля — Ado STADIUM LIVE 2026 «Ao».
• 7 августа — фильм «Blue Lock» с песней «MONSTRUO».
• На 6 ноября запланирован релиз/премьерный показ
  аниме «Demon's Crest» с новой песней «Shinka».
""",

    "achievements": """
🏆 ДОСТИЖЕНИЯ

• «Usseewa» стала одним из крупнейших дебютов
  японской интернет-сцены и достигла №1 в
  Billboard Japan Hot 100.

• Ado стала первой женщиной-сольной исполнительницей,
  проведшей сольный концерт на Национальном стадионе
  Японии.

• Ado SPECIAL LIVE 2024 «Shinzou» собрал более
  140 000 зрителей за два дня.

• Первый мировой тур «Wish» стал важным этапом
  международного выхода Ado.

• Ado WORLD TOUR 2025 «Hibana» прошёл в 33 городах
  и собрал более 500 000 зрителей.

• «Hibana» стал одним из крупнейших мировых туров
  японского артиста.

• В 2025 году Ado выпустила свой первый best album
  «Ado's Best Adobum» — 40 треков на двух CD.

• В первой половине 2026 года Ado заняла первое место
  среди японских артистов по зарубежным прослушиваниям
  в Spotify.

• В 2026 году Ado провела стадионный концерт
  «Ao» на Nissan Stadium.
""",

    "music": """
🎵 МУЗЫКАЛЬНЫЙ ПУТЬ

Ado выросла из интернет-культуры utaite и Vocaloid.

Ещё до дебюта она слушала Vocaloid, смотрела
«歌ってみた» и вдохновлялась тем, как исполнители
могут создавать отдельный образ только голосом.

В её каталоге работают разные авторы и продюсеры:
Vocaloid-продюсеры, композиторы поп-музыки,
рок-музыканты и авторы саундтреков.

Одна из особенностей Ado — способность резко менять
характер вокала внутри одной песни: от мягкого
и почти шёпотного звучания до агрессивной подачи,
гроула и очень мощных верхних нот.

При этом Ado остаётся именно исполнителем:
большая часть её известных песен написана другими
авторами, а сама Ado превращает их в собственные
вокальные образы.
""",

    "projects": """
🎬 ПРОЕКТЫ

🏴‍☠️ ONE PIECE FILM RED
Ado стала вокальным голосом Уты и исполнила
вокал для песен фильма.

🐈 CAT'S EYE
Ado исполнила новую музыкальную тему проекта:
«CAT'S EYE» и написанную специально для аниме
«MAGIC».

👻 GEGEGE NO KITARO
Ado стала исполнительницей новой версии
знаменитой темы «GeGeGe no Kitaro».

🌸 CHIBI MARUKO-CHAN
Ado исполнила «Odoru Ponpokorin» для обновлённой
версии опенинга.

⚽ BLUE LOCK
«MONSTRUO» стала заглавной песней игрового фильма
«Blue Lock», вышедшего в августе 2026 года.

🎮 RHYTHM HEAVEN
«Love me forever!» была написана для новой игры
«Rhythm Heaven Miracle Stars».

📺 DEMON'S CREST
Для аниме «Demon's Crest» заявлена новая песня
«Shinka» с премьерой проекта в ноябре 2026 года.
""",
}


def about_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📖 Биография",
                    callback_data="about_bio"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📅 Хронология",
                    callback_data="about_timeline"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🏆 Достижения",
                    callback_data="about_achievements"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🎵 Музыкальный путь",
                    callback_data="about_music"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🎬 Проекты",
                    callback_data="about_projects"
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
    "Motherland",
    "FREEDOM",
    "Domestic De Violence",
    "Fireworks",
    "Lucky Bruto",
    "KokoroToIuNaNoFukakai",
    "Kagakushu",

    "New Genesis",
    "I'm Invincible",
    "Backlight",
    "Fleeting Lullaby",
    "Tot Musica",
    "The World's Continuation",
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
    "Episode X",

    "Nukegara",
    "The Story of the Wind and I",
    "Elf",
    "Bouquet for Me",
    "MAGIC",
    "ROCKSTAR",
    "Hello Signals",
    "0",

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
    "Dried Flowers",
    "Kazari ja Nai no yo Namida wa",
    "Aishite Aishite Aishite",
    "Crime and Punishment",
    "Kawaikute Gomen",
    "Villain",
    "God-ish",
    "Unravel",
    "Buriki No Dance",
    "Dawn and Fireflies",
    "CAT'S EYE",
    "GeGeGe no Kitaro",
    "Odoru Ponpokorin",
    "soldier game"
]


# ============================================================
# 🤝 КОЛЛАБОРАЦИИ
# ============================================================

COLLABS = [
    "Take Me to the Beach — Imagine Dragons feat. Ado",
    "UNFORGIVEN — LE SSERAFIM feat. Ado",
    "Stay Gold — Jax Jones & Ado",
    "Sakura Biyori and Time Machine with Hatsune Miku"
]


# ============================================================
# 🏴‍☠️ ONE PIECE FILM: RED
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
        "Readymade",
        "Odo",
        "Domestic De Violence",
        "FREEDOM",
        "Fireworks",
        "Aitakute",
        "Lucky Bruto",
        "Gira Gira",
        "Ashura-chan",
        "KokoroToIuNaNoFukakai",
        "Usseewa",
        "Motherland",
        "Kagakushu",
        "Yoru no Pierrot"
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
        "Dried Flowers",
        "Kazari ja Nai no yo Namida wa",
        "Aishite Aishite Aishite",
        "Crime and Punishment",
        "Kawaikute Gomen",
        "Villain",
        "God-ish",
        "Unravel",
        "Buriki No Dance",
        "Dawn and Fireflies"
    ],

    "Zanmu": [
        "Nukegara",
        "Where the Uncertainty Is",
        "Dignity",
        "Chocolat Cadabra",
        "Kura Kura",
        "I'm a Controversy",
        "Rebellion",
        "All Night Radio",
        "Himawari",
        "Eien no Akuruhi",
        "Mirror",
        "RuLe",
        "Show",
        "Ibara",
        "Value",
        "0"
    ],

    "Ado's Best Adobum": [
        "Usseewa",
        "Ashura-chan",
        "Yoru no Pierrot",
        "Kura Kura",
        "Chocolat Cadabra",
        "Unravel",
        "I'm Invincible",
        "Fleeting Lullaby",
        "Motherland",
        "Himawari",
        "New Genesis",
        "Gira Gira",
        "RuLe",
        "Episode X",
        "FREEDOM",
        "ROCKSTAR",
        "Show",
        "Ibara",
        "Value",
        "KokoroToIuNaNoFukakai",
        "Shoka",
        "Hello Signals",
        "Backlight",
        "Rebellion",
        "Mirror",
        "I'm a Controversy",
        "Missing",
        "Aishite Aishite Aishite",
        "Tot Musica",
        "Dignity",
        "Aitakute",
        "Elf",
        "Eien no Akuruhi",
        "Readymade",
        "Lucky Bruto",
        "Kagakushu",
        "All Night Radio",
        "Bouquet for Me",
        "Odo",
        "Sakura Biyori and Time Machine with Hatsune Miku"
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
# 🌟 ФАКТЫ
# ============================================================

FACTS_TEXT = """
🌟 ФАКТЫ ОБ ADO

🎙️ Ado выросла из интернет-культуры utaite и Vocaloid.
Ещё в детстве она интересовалась Vocaloid-музыкой.

🚪 До мейджор-дебюта она записывала каверы дома,
используя шкаф как место с меньшим количеством отражений.

🧎 Даже в профессиональной студии Ado привыкла
записывать вокал сидя со скрещёнными ногами.

🎧 При записи оригинальных песен она предпочитает
работать очень самостоятельно: в студии может находиться
одна, со своим компьютером, а готовый материал отправляет
после записи.

🍣 Одно из её любимых блюд — суши. В интервью Ado также
называла тунец своим любимым видом суши.

👻 Ado с детства любит «GeGeGe no Kitaro» и японскую
тему ёкаев; любовь к Kitaro стала одной из причин её
участия в проекте «GeGeGe no Kitaro».

🎮 До профессиональной карьеры Ado не только слушала
Vocaloid, но и смотрела игровые видео, танцевальные видео
и музыкальные MAD-видео на NicoNico.

💬 Ей нравился формат NicoNico с прокручивающимися
комментариями, и ей хотелось однажды увидеть такие
комментарии под собственным видео.

🎭 Анонимность для Ado связана не только с внешностью:
она делает основной акцент на голосе, музыке и образе,
а не на публичном показе лица.

🎤 Ado известна тем, что использует очень широкий
диапазон вокальных приёмов и может резко менять
характер исполнения внутри одной композиции.

🛋️ В свободное время Ado любит расслабляться дома,
смотреть сериалы и заниматься покупками одежды и
косметики.

🎀 Ado особенно любит Hatsune Miku; в 2024 году они
впервые вместе выступили на сцене с
«Sakura Biyori and Time Machine».
"""

# ============================================================
# 🌟 ФАКТЫ
# ============================================================

@dp.callback_query(F.data == "facts")
async def facts(callback: CallbackQuery):

    await callback.message.edit_text(
        FACTS_TEXT,
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
        reply_markup=about_menu()
    )

    await callback.answer()


# ============================================================
# 📖 ПОДРАЗДЕЛЫ «ОБ ADO»
# ============================================================

@dp.callback_query(F.data.startswith("about_"))
async def about_section(callback: CallbackQuery):

    section = callback.data.replace("about_", "", 1)
    text = ABOUT_SECTIONS.get(section)

    if text is None:
        await callback.answer("Раздел не найден.", show_alert=True)
        return

    await callback.message.edit_text(
        text,
        reply_markup=about_menu()
    )

    await callback.answer()

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

import os
from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application


TOKEN = os.getenv("BOT_TOKEN")

WEBHOOK_PATH = "/webhook"
WEBHOOK_HOST = os.getenv("RENDER_EXTERNAL_HOSTNAME")
WEBHOOK_URL = f"https://{WEBHOOK_HOST}{WEBHOOK_PATH}"


async def on_startup(bot: Bot):
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(bot: Bot):
    await bot.delete_webhook()

async def health(request):
    return web.Response(text="Ado Info Bot is alive!")
    
    
def main():
    bot = Bot(TOKEN)

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    app = web.Application()
app.router.add_get("/", health)

    webhook_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot
    )

    webhook_handler.register(
        app,
        path=WEBHOOK_PATH
    )

    setup_application(app, dp, bot=bot)

    port = int(os.getenv("PORT", 10000))

    web.run_app(
        app,
        host="0.0.0.0",
        port=port
    )


if __name__ == "__main__":
    main()
