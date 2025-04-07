import discord 
import config
from discord.ext import commands 
# from discord import app_commands
import random
intents = discord.Intents.all()
intents.message_content = True
intents.members = True
intents.guilds = True
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)


bot = commands.Bot(command_prefix="!", intents=intents)

# Define a hybrid command
@bot.hybrid_command(name="greet", description="Greets the user")
async def greet(ctx: commands.Context, name: str):
    await ctx.send(f"Hello, {name}!")

@bot.hybrid_command(name="roll", description="roll your dice")
async def roll(ctx: commands.Context, dice: int):
    roll = random.randint(1, dice)
    await ctx.send(f"You rolled a {dice} and got  {roll}!")

@bot.event
async def on_ready():
    # print(f'Your client is {client.get_guild}')
    # await tree.sync(guild=discord.Object(id=512714223831220235))
    await bot.tree.sync()
    print(f'We have logged in as {bot.user}')
    

# @client.event
# async def on_ready():
#     print(f'We have logged in as {client.user}')
# @tree.command(name="hello",description="Say hello to the bot!")
# async def slash_command(interaction: discord.Interaction):
#     await interaction.response.send_message("Hello!")

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content == ('$hello'):
#         await message.channel.send('Hello!')

#     if message.content == ('$d20'):
#         await message.channel.send(random.randint(1, 20))

#     if message.content == ('$d6'):
#         await message.channel.send(random.randint(1, 6))

#     if message.content == ('$d4'):    
#         await message.channel.send(random.randint(1, 4))

#     if message.content == ('$d8'):    
#         await message.channel.send(random.randint(1, 8))

#     if message.content == ('$d10'):   
#         await message.channel.send(random.randint(1, 10))

#     if message.content == ('$d12'):    
#         await message.channel.send(random.randint(1, 12))

#     if message.content == ('$d100'):  
#         await message.channel.send(random.randint(1, 100))


bot.run(config.api_key)
#@client.event

#client.run(config.api_key)