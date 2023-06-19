





#
#  good emoji
#  finally some good f**ing emoji
#

import discord
import psutil
import os
import sqlite3
from sqlite3 import Error
from discord.commands import OptionChoice, Option 

bot = discord.Bot()

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
        :param db_file: database file
        :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

@bot.event
async def on_ready():
    print(f"Ready and logged in as {bot.user}!")
    game = discord.Game("No More MEE6!")
    await bot.change_presence(status=discord.Status.online, activity=game)

def get_current(category):
  conn = create_connection(r"./goodemoji.sqlite3")
  if conn is not None:
    c = conn.cursor()
    c.execute("SELECT "+category+" FROM emoji;")
    value = c.fetchone()
    return value;
  else:
    print("Error! cannot create the database connection.")

def add_one(category):
  conn = create_connection(r"./goodemoji.sqlite3")
  value = get_current(category)
  beforebeforenewvalue = ''.join(map(str, value))
  oldvalue = str(beforebeforenewvalue)
  beforenewvalue = int(beforebeforenewvalue) + 1
  newvalue = str(beforenewvalue)
  if conn is not None:
    c = conn.cursor()
    c.execute("UPDATE emoji SET "+category+" = "+newvalue+" WHERE "+category+" = "+oldvalue+";")
    conn.commit()
  else:
    print("Error! cannot create the database connection.")




# UPDATE THE EMOJILIST COMMAND. DO IT.
pos = [
    OptionChoice(name="Angel", value="/angel"),
    OptionChoice(name="Blush", value="/blush"),
    OptionChoice(name="Cool", value="/cool"),
    OptionChoice(name="Look", value="/look"),
    OptionChoice(name="Love", value="/love"),
    OptionChoice(name="Nice", value="/nice"),
    OptionChoice(name="Silly", value="/silly"),
    OptionChoice(name="Sleep", value="/sleep"),
    OptionChoice(name="Smile", value="/smile"),
    OptionChoice(name="Think", value="/think"),
    OptionChoice(name="No More MEE6", value="/nomoremee6"),
]
# UPDATE THE EMOJILIST COMMAND. DO IT.
neu = [
    OptionChoice(name="Shh", value="/shh"),
    OptionChoice(name="Whistle", value="/whistle"),
    OptionChoice(name="Worship & Prayer", value="/worshipandprayer"),
    OptionChoice(name="Unamused", value="/unamused"),
    OptionChoice(name="Shout", value="/shout"),
    OptionChoice(name="Shrug", value="/shrug"),
    OptionChoice(name="Call", value="/call"),
    OptionChoice(name="Chef", value="/chef"),
    OptionChoice(name="Gasp", value="/gasp"),
    OptionChoice(name="No Thanks", value="/nothanks"),
]
# UPDATE THE EMOJILIST COMMAND. DO IT.
neg = [
    OptionChoice(name="Angry", value="/angry"),
    OptionChoice(name="Violence", value="/violence"),
    OptionChoice(name="Sad", value="/sad"),
    OptionChoice(name="Stomp Away", value="/stompaway"),
    OptionChoice(name="No Bitches", value="/nobitches"),
    OptionChoice(name="Pointing", value="/pointing"),
    OptionChoice(name="Idea", value="/idea"),
    OptionChoice(name="Cry", value="/cry"),
]
# UPDATE THE EMOJILIST COMMAND. DO IT.
pou = [
    OptionChoice(name="Hungry Stare", value="/starehungry"),
    OptionChoice(name="Hungry Sick Yell", value="/sickhungryyell"),
    OptionChoice(name="Sick Yell", value="/sick"),
    OptionChoice(name="Sick", value="/sick"),
    OptionChoice(name="Stare", value="/stare"),
    OptionChoice(name="Suspicious", value="/suspicious"),
    OptionChoice(name="Yell", value="/yell"),
    OptionChoice(name="I Am Hungry", value="/iamhungry"),
    OptionChoice(name="Sick Stare", value="/sickstare"),
    OptionChoice(name="Sick Cough", value="/sickcough"),
    OptionChoice(name="Sick Look", value="/sicklook"),
    OptionChoice(name="Sick Look Up", value="/sicklookup"),
]
# UPDATE THE EMOJILIST COMMAND. DO IT.

@bot.command(description="Send one of the best emojis", cooldown=None)
async def emoji(ctx):
  emojilist = discord.Embed(title="Each category is it's own command", color=0x2f3136)
  emojilist.add_field(name="Positive", value="Angel, Blush, Cool, Look, Love, Nice, Silly, Sleep, Smile, Think, No More MEE6", inline=True)
  emojilist.add_field(name="Neutral", value="Shh, Whistle, Worship & Prayer, Unamused, Shout, Shrug, Call, Chef, Gasp, No Thanks", inline=True)
  emojilist.add_field(name="Negative", value="Angry, Violence, Sad, Stomp Away, No Bitches, Pointing, Idea, Cry", inline=True)
  await ctx.respond(embed=emojilist)

@bot.command(description="Statistics on global good emoji usage", cooldown=None)
async def statistics(ctx):
  posnum = int(''.join(map(str, get_current('positive'))))
  neunum = int(''.join(map(str, get_current('neutral'))))
  negnum = int(''.join(map(str, get_current('negative'))))
  emojistats = discord.Embed(title="Statistics on global emoji usage", color=0x2f3136)
  emojistats.add_field(name="Positive", value=f"Used {posnum} times", inline=True)
  emojistats.add_field(name="Neutral", value=f"Used {neunum} times", inline=True)
  emojistats.add_field(name="Negative", value=f"Used {negnum} times", inline=True)
  emojistats.set_footer(text=f"Used a total of {posnum+neunum+negnum} times")
  await ctx.respond(embed=emojistats)

@bot.command(description="Information about good emoji", cooldown=None)
async def info(ctx):

  load1, load5, load15 = psutil.getloadavg()
  total_memory, used_memory, free_memory = map(
    int, os.popen('free -t -m').readlines()[-1].split()[1:])
  cpu_usage = (load15/os.cpu_count()) * 100

  infolist = discord.Embed(title="Information about good emoji", color=0x2f3136)
  infolist.add_field(name="RAM Usage", value=f"{round((used_memory/total_memory) * 100, 2)}%", inline=True)
  infolist.add_field(name="CPU Usage", value=f"{round(cpu_usage)}%", inline=True)
  infolist.add_field(name="Servers", value=f"In {str(len(bot.guilds))} servers", inline=True)
  infolist.add_field(name="Ping", value=f"{round (bot.latency * 1000)}ms", inline=True)
  infolist.add_field(name="System", value="Ubuntu 22.04.1 LTS", inline=True)
  infolist.add_field(name="Architecture", value="x86_64", inline=True)
  await ctx.respond(embed=infolist)

@bot.command(description="Send one of the best positive emojis", cooldown=None)
async def positive(ctx, emoji: Option(name="positive", description="List of positive emojis", choices=pos)):
  path = "./assets"
  c = path + emoji + ".png"
  await ctx.respond(file=discord.File(c))
  print("Sent positive emoji " + emoji + ".")
  add_one("positive")

@bot.command(description="Send one of the best neutral emojis", cooldown=None)
async def neutral(ctx, emoji: Option(name="neutral", description="List of neutral emojis", choices=neu)):
  path = "./assets"
  c = path + emoji + ".png"
  await ctx.respond(file=discord.File(c))
  print("Sent neutral emoji " + emoji + ".")
  add_one("neutral")

@bot.command(description="Send one of the best negative emojis", cooldown=None)
async def negative(ctx, emoji: Option(name="negative", description="List of negative emojis", choices=neg)):
  path = "./assets"
  c = path + emoji + ".png"
  await ctx.respond(file=discord.File(c))
  print("Sent negative emoji " + emoji + ".")
  add_one("negative")

@bot.command(description="Send one of the best Pou emojis", cooldown=None)
async def pou(ctx, emoji: Option(name="pou", description="List of Pou emojis", choices=pou)):
  path = "./assets/pou"
  c = path + emoji + ".png"
  await ctx.respond(file=discord.File(c))
  print("Sent Pou emoji " + emoji + ".")


bot.run("")
