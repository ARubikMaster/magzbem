import discord
from discord.ext import commands
from discord import app_commands


bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1292663435783307381)
    embed = discord.Embed(
        title=f"Welcome {member}",
        description="Make sure to read the rules and additional information",
        color=discord.Color.blue()
    )
    embed.set_image(url="https://media.discordapp.net/attachments/1106364504805228606/1293664513077280992/Discord_Images.png?ex=67116cf7&is=67101b77&hm=2c9b6207377cf058fac685148f238315f0f628fd50236c021aba89462956011c&=&format=webp&quality=lossless&width=1439&height=562")  # Replace IMAGE_URL_HERE with the link to your image

    await channel.send(embed=embed)
    await member.send(embed=embed)

async def setup_hook():
    await bot.tree.sync()

bot.setup_hook = setup_hook
bot.run('MY_API_KEY')
