from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📝 Yangi e'lon")],
        [KeyboardButton(text="📅 Rejalashtirilgan e'lonlar")],
        [KeyboardButton(text="📤 Hozir yuborish")],
        [KeyboardButton(text="📚 E'lonlar arxivi")],
        [KeyboardButton(text="📊 Statistika")],
        [KeyboardButton(text="⚙️ Sozlamalar")]
    ],
    resize_keyboard=True
)
