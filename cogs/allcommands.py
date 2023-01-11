import disnake
import asyncio
import random
from disnake.ext import commands
from disnake import TextInputStyle


class Command(commands.Cog):
	def __init__(self, bot:commands.Bot):
		self.bot=bot


	@commands.command()
	@commands.has_permissions()
	async def help (self, ctx):
		emb=disnake.Embed(title='Доступные команды', color=0x5e17a6)
		emb.add_field(name='!kick', value='Удаление участника с сервера', inline=False)
		emb.add_field(name='!ban', value= 'Ограничение доступа к серверу', inline=False)
		emb.add_field(name='!mute', value= 'Ограничение текстовых и голосовых каналов', inline=False)
		emb.add_field(name='!clear', value= 'Очистка текстовых каналов', inline=False)
		emb.add_field(name='!bullet', value= 'Игра русская рулетка', inline=False)
		emb.add_field(name='/say', value= 'Отправить сообщение от имени бота', inline=False)
		emb.add_field(name='/offer', value= 'Предложить свои команды для бота', inline=False)
		await ctx.send(embed=emb)


	@commands.command()
	@commands.has_permissions(kick_members=True, administrator=True)
	async def kick(self, ctx, member: disnake.Member, *, reason="Нарушение правил."):
		await ctx.send(f"{ctx.author.mention} выгнал непослушную морковку {member.mention}", delete_after=5)
		await member.kick(reason=reason)
		await ctx.message.delete()
		print(f"{member} кикнут")


	@commands.command()
	@commands.has_permissions( ban_members=True, administrator=True)
	async def ban(self, ctx, member: disnake.Member, *, reason="Нарушение правил."):
		await ctx.send(f"{ctx.author.mention} уничтожил непослушную морковку {member.mention}", delete_after=5)
		await member.ban(reason=reason)
		await ctx.message.delete()
		print(f"{member} забанен")


	@commands.command()
	@commands.has_permissions(administrator=True)
	async def mute(self, ctx, member: disnake.Member, time: int):
		await ctx.channel.purge(limit=1)
		await ctx.send(f"{ctx.author.mention} заклеил рот плохой морковке {member.mention}", delete_after=5)
		muted_role = disnake.utils.get(ctx.message.guild.roles, id=1048612028866113596)
		await member.add_roles(muted_role)
		print(f"выдан мут {member}")
		await asyncio.sleep(time)
		await member.remove_roles(muted_role)
		print(f"мут снят c {member}")


	@commands.command()
	@commands.has_permissions(administrator=True)
	async def clear(self, ctx,user: disnake.Member,amount: int=100):
		await ctx.channel.purge(limit=amount, check=lambda m: m.author==user)
		print(f"Чат очищен")
		await ctx.message.delete()


	@commands.command()
	@commands.has_permissions()
	async def bullet (self, ctx):
		words_list = ["спускает курок и ничего не происходит", "спускает курок и раздаётся выстрел"]
		random_word = random.choice(words_list)
		await ctx.message.delete()
		await ctx.send(f"{ctx.author.mention} {random_word}")


	@commands.slash_command(name='say',description="Написать текст от имени бота")
	async def say(self, interaction: disnake.CommandInteraction, message: str):
		await interaction.channel.send(message)
		await interaction.send("Отправлено", ephemeral=True)


def setup(bot: commands.Bot):
	bot.add_cog(Command(bot))
	print(f">{__name__} готов к работе")