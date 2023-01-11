import disnake
import asyncio
import os
from disnake.ext import commands
from disnake import TextInputStyle

bot=commands.Bot(command_prefix = "!", help_command = None, intents = disnake.Intents.all(), activity = disnake.Game('Кролика | !help', status = disnake.Status.online ),test_guilds=[1006862374411714581])


bot.load_extension("cogs.modals")
bot.load_extension("cogs.allcommands")
bot.load_extension("cogs.eventg")
bot.load_extension("cogs.music")


bot.run("MTA0NzkxMzU2MTY4NDQ1NTQ1NA.GehPlQ.mAM_tThDuu5l1XQJ3tpwBDZ1p3nXL7IbS8iQgQ")