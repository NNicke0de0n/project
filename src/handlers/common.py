from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    """Обработчик команды /start."""
    await message.answer(
        "Привет! Я HabitTrackerBot — твой помощник для трекинга привычек.\n"
        "Используй /help, чтобы посмотреть доступные команды."
    )

@router.message(Command("help"))
async def cmd_help(message: Message):
    """Обработчик команды /help."""
    await message.answer(
        "Доступные команды:\n"
        "/start — Главное меню\n"
        "/add — Добавить новую привычку\n"
        "/list — Список моих привычек\n"
        "/stats — Статистика выполнения"
    )