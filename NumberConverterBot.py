# NumberConverterBot.py
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import filters
from aiogram.utils import executor

# Ваш токен
API_TOKEN = 'YOUR_API_TOKEN_HERE'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Словари для преобразования чисел в слова
ONES = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
TEENS = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
TENS = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
THOUSANDS = ["", "Thousand"]

ONES_RU = ["", "Один", "Два", "Три", "Четыре", "Пять", "Шесть", "Семь", "Восемь", "Девять"]
TEENS_RU = ["Десять", "Одиннадцать", "Двенадцать", "Тринадцать", "Четырнадцать", "Пятнадцать", "Шестнадцать", "Семнадцать", "Восемнадцать", "Девятнадцать"]
TENS_RU = ["", "", "Двадцать", "Тридцать", "Сорок", "Пятьдесят", "Шестьдесят", "Семьдесят", "Восемьдесят", "Девяносто"]
THOUSANDS_RU = ["", "Тысяча"]

def number_to_words(num: int, lang: str):
    if num == 0:
        return "Zero" if lang == 'en' else "Ноль"

    if lang == 'en':
        words = ""
        thousands = num // 1000
        hundreds = (num % 1000) // 100
        tens_units = num % 100

        if thousands > 0:
            words += ONES[thousands] + " " + THOUSANDS[1] + " "
        if hundreds > 0:
            words += ONES[hundreds] + " Hundred "
        if tens_units >= 10 and tens_units < 20:
            words += TEENS[tens_units - 10] + " "
        else:
            tens = tens_units // 10
            units = tens_units % 10
            if tens > 0:
                words += TENS[tens] + " "
            if units > 0:
                words += ONES[units] + " "

        return words.strip()

    else:  # для русского
        words = ""
        thousands = num // 1000
        hundreds = (num % 1000) // 100
        tens_units = num % 100

        if thousands > 0:
            words += str(ONES_RU[thousands]) + " " + THOUSANDS_RU[1] + " "
        if hundreds > 0:
            words += str(ONES_RU[hundreds]) + " Сотня "
        if tens_units >= 10 and tens_units < 20:
            words += str(TEENS_RU[tens_units - 10]) + " "
        else:
            tens = tens_units // 10
            units = tens_units % 10
            if tens > 0:
                words += str(TENS_RU[tens]) + " "
            if units > 0:
                words += str(ONES_RU[units]) + " "

        return words.strip()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Здравствуйте! Введите неотрицательное целое число для преобразования.")

@dp.message_handler()
async def convert_number(message: types.Message):
    try:
        num = int(message.text)
        if num < 0:
            raise ValueError("Число должно быть неотрицательным.")
        # Преобразуйте число на оба языка
        en_word = number_to_words(num, 'en')
        ru_word = number_to_words(num, 'ru')
        await message.reply(f"На английском: {en_word}\nНа русском: {ru_word}")
    except ValueError as e:
        await message.reply("Ошибка! Пожалуйста, введите корректное неотрицательное целое число.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
