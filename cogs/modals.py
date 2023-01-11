import disnake
import asyncio
from disnake.ext import commands
from disnake import TextInputStyle


class Modal(disnake.ui.Modal):
	def __init__(self):
		components = [
			disnake.ui.TextInput(
				label="Назнвание",
				placeholder="Как вы хотите назвать команду",
				custom_id="название",
				style=TextInputStyle.short,
				max_length=50,
			),
			disnake.ui.TextInput(
				label="Краткое описание",
				placeholder="Опишите как должна работать ваша команда",
				custom_id="описание",
				style=TextInputStyle.paragraph,
			),
		]
		super().__init__(
			title="Предложения",
			custom_id="Предложения",
			components=components,
		)
	async def callback(self, inter: disnake.ModalInteraction):
		embed = disnake.Embed(title="Предложения",color=0x5e17a6)
		for key, value in inter.text_values.items():
			embed.add_field(
				name=key.capitalize(),
				value=value[:1024],
				inline=False,
			)
		await inter.response.send_message(embed=embed)


class Modals(commands.Cog):
	def __init__(self, bot:commands.Bot):
		self.bot=bot


	@commands.slash_command(name='offer',description="Форма для предложения своей команды")
	async def offer(self, inter: disnake.AppCmdInter):
		await inter.response.send_modal(modal=Modal())


def setup(bot: commands.Bot):
	bot.add_cog(Modals(bot))
	print(f">{__name__} готов к работе")