import disnake
import wavelink
import typing
import os
from disnake.ext import commands


class Music(commands.Cog):
	def __init__(self, bot:commands.Bot):
		self.bot=bot
		self.playingTextChannel = 0
		bot.loop.create_task(self.connect_nodes())
	async def connect_nodes(self):
		await self.bot.wait_until_ready()
		await wavelink.NodePool.create_node(bot=self.bot,host="lavalink-replit.filsbrik.repl.co", https="lavalink-replit.filsbrik.repl.co", port="443", password="BunnySempai", region="asia")


	@commands.command(name="play",aliases=["p"])
	async def play(self, ctx: commands.Context, *, search: wavelink.YouTubeTrack):
		if not ctx.voice_client:
			vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
		else:
			vc: wavelink.Player = ctx.voice_client
		await vc.play(search)
		mbed = disnake.Embed(
			title=f"Сейчас играет: {search}",
			color=0x5e17a6
			)

		t_sec = int(search.length)
		hour = int(t_sec/3600)
		min = int((t_sec%3600)/60)
		sec = int((t_sec%3600)%60)
		length = f"{hour}h {min}min {sec}sec" if not hour == 0 else f"{min}min {sec}sec"

		mbed.add_field(name="Исполнитель", value=search.info['author'])
		mbed.add_field(name="Продолжительность", value=f"{length}")
		await ctx.send(embed=mbed)


	@commands.command(name="stop",aliases=["s"])
	async def stop(self, ctx: commands.Context):
		node = wavelink.NodePool.get_node()
		player = node.get_player(ctx.guild)
		if player is None:
			return await ctx.send("Бот не подключен ни к одному из голосовых каналов")
		if player.is_playing:
			await player.stop()
			mbed = disnake.Embed(title="Воспроизведение остановлено",color=0x5e17a6)
			return await ctx.send(embed=mbed)
		else:
			return await ctx.send("Сейчас ничего не играет")


	@commands.command(name="pause",aliases=["ps"])
	async def pause(self, ctx: commands.Context):
		node = wavelink.NodePool.get_node()
		player = node.get_player(ctx.guild)
		if player is None:
			return await ctx.send("Бот не подключен ни к одному из голосовых каналов")
		if not player.is_paused():
			if player.is_playing():
				await player.pause()
				mbed = disnake.Embed(title="Воспроизведение приостановлено",color=0x5e17a6)
				return await ctx.send(embed=mbed)
			else:
				return await ctx.send("Сейчас ничего не играет")
		else:
			return await ctx.send("Воспроизведение уже приостановлено")


	@commands.command(name="resume",aliases=["rs"])
	async def resume(self, ctx: commands.Context):
		node = wavelink.NodePool.get_node()
		player = node.get_player(ctx.guild)
		if player is None:
			return await ctx.send("Бот не подключен ни к одному из голосовых каналов")
		if player.is_paused():
			await player.resume()
			mbed = disnake.Embed(title="Воспроизведение возобновилось",color=0x5e17a6)
			return await ctx.send(embed=mbed)
		else:
			return await ctx.send("Воспроизведение не приостановлено")


def setup(bot: commands.Bot):
	bot.add_cog(Music(bot))
	print(f">{__name__} готов к работе")