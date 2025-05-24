from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext
from app.generate import ai_generate
import app.keyboard as kb
router = Router()

@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer("Добро пожаловать в бесплатный Deepseek в telegram! \n"
                         "Напишите ваш запрос и подпишитесь на канал:https://t.me/DeepSeekFun2025\n"
                         "Ваш донат мне очень поможет",reply_markup=kb.donate)

class Gen(StatesGroup):
    wait = State()
@router.message(Gen.wait)
async def sop_flood(message:Message):
    await message.answer("Пожалуйста подождите")#вставить смайлик

@router.message()
async def generating(message:Message,state:FSMContext):
    await state.set_state(Gen.wait)
    response = await ai_generate(message.text)
    await message.answer(response)
    await state.clear()

