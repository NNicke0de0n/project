from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("list"))
async def cmd_list_habits(message: Message):
    """Вывод списка активных привычек пользователя."""
    # Заглушка выборки из БД до подключения CRUD-слоя
    await message.answer(
        "Ваши активные привычки:\n"
        "1. Пить воду — 09:00\n"
        "2. Чтение книги — 21:00\n\n"
        "(Список сформирован в тестовом режиме)"
    )

async def cmd_add_habit(message):
    """Добавление новой привычки для трекинга."""
    pass

async def cmd_list_habits(message):
    """Вывод списка всех привычек пользователя."""
    pass

async def cmd_check_habit(message):
    """Отметка выполнения привычки за текущий день."""
    pass


