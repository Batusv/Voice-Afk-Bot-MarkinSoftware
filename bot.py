import discord
import config  # config.py dosyasını içe aktarıyoruz
import os

# Token'ı config.py dosyasından al
bottoken = config.BOT_TOKEN

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def join_voice(ctx):
    # Kullanıcının bulunduğu ses kanalını al
    channel = ctx.author.voice.channel if ctx.author.voice else None
    if not channel:
        await ctx.send("Bir ses kanalında değilsiniz!")
        return

    # Botun mevcut ses bağlantısını kontrol et
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client and voice_client.is_connected():
        # Eğer bot zaten bir ses kanalına bağlıysa
        await ctx.send("Bot zaten bir ses kanalına bağlı!")
        return

    # Kanala bağlan
    await channel.connect()
    await ctx.send(f"{channel.name} kanalına bağlandım! discord.gg/markincode")

@bot.command()
async def join(ctx):
    # Kullanıcının ses kanalında olup olmadığını kontrol et
    if ctx.author.voice:
        channel = ctx.author.voice.channel  # Kullanıcının olduğu ses kanalını al
        await channel.connect()  # Bot kanala katılır
        await ctx.send(f"{channel.name} kanalına katıldım! discord.gg/markincode")
    else:
        await ctx.send("Önce bir ses kanalına katılmalısın! discord.gg/markincode")

@bot.command()
async def leave(ctx):
    # Botun bir ses kanalında olup olmadığını kontrol et
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Ses kanalından ayrıldım! discord.gg/markincode")
    else:
        await ctx.send("Ses kanalında değilim! discord.gg/markincode")


# Botu başlat
bot.run(bottoken)
