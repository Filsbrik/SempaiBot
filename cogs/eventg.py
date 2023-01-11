import disnake
import asyncio
import random
from disnake.ext import commands
from disnake import TextInputStyle


class Event(commands.Cog):
	def __init__(self, bot):
		self.bot=bot


	@commands.Cog.listener()
	async def on_member_join(self, member):
		role=disnake.utils.get(member.guild.roles, id=1006868272119037952)
		channel=self.bot.get_channel(1020321609107652728)
		embed=disnake.Embed(
			title="",
			description=f"Привет {member.mention}, добро пожаловать в нашу **нору**!",
			color=disnake.Colour.random())
		embed.set_image(url="https://i.imgur.com/lHufqpx.jpg")
		await member.add_roles(role)
		await channel.send(embed=embed)
		print(f"{member} выдана роль {role}")


	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		print(error)
		if isinstance(error, commands.MissingPermissions):
			await ctx.send(f"{ctx.author.mention}, ваша морковка не нуждается в этом!", delete_after=3)
		elif isinstance(error, commands.UserInputError):
			await ctx.send(embed=disnake.Embed(
				description=f"Правильное делать вот так: '{ctx.prefix}{ctx.command.name}' ({ctx.command.brief})\nExample: {ctx.prefix}{ctx.command.usage}",), delete_after=3)
		await ctx.message.delete()


def setup(bot: commands.Bot):
	bot.add_cog(Event(bot))
	print(f">{__name__} готов к работе")