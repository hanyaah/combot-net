from discord.ext import commands

description = '''A bot to connect the playerbase of multiple Tekken discords using their platform and ID.'''

#   specifies extensions to load when bot starts up
startup_extensions = ["Players"]

bot = commands.Bot(command_prefix='.', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def hello():
    """Say hi!"""
    await bot.say("Hello!")

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run('token')