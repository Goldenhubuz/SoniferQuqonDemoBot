from aiogram import Bot
from aiogram.methods.set_my_commands import BotCommand
from aiogram.types import BotCommandScopeDefault, BotCommandScopeChat

import config

async def set_default_commands(bot: Bot):
    # Commands for everyone
    default_commands = [
        BotCommand(command="start", description="Botni ishga tushirish"),
        BotCommand(command="help", description="Yordam markazi"),
        BotCommand(command="categories", description="Barcha kategoriyalar"),
        BotCommand(command="my_profile", description="Mening ma'lumotlarim"),
        BotCommand(command="faq", description="Qoidalar"),
        BotCommand(command="cart", description="Savat"),
    ]
    await bot.set_my_commands(commands=default_commands, scope=BotCommandScopeDefault())

    # Commands for administrators
    admin_commands = default_commands + [
        BotCommand(command="panel", description="Boshqaruv paneli"),
    ]

    for admin in config.ADMIN_ID_LIST:
        await bot.set_my_commands(admin_commands, scope=BotCommandScopeChat(chat_id=admin))
