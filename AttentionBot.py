import discord
from discord.ext import commands
import datetime
import schedule
import threading
intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents = intents)
user_status = "none"
bot = commands.Bot(command_prefix= '!')
nameuser = "Dodoris#0892"
msgstatuser = "0"
@client.event
async def on_message(message):
    global msgstatuser
    print(message.author)
    if ((str(message.author)) == nameuser) and msgstatuser == "0":
        msgstatuser = "1"
        print(message.author, msgstatuser)
        await message.channel.send("АТЕНШОН, НЕУЧЕБНАЯ ТРЕВОГА!!! В THIS GYM ПРОБРАЛАСЬ ЖЕНЩИНА ПО ИМЕНИ ДАРЬЯ!!! DUNGEON MASTER ПРИКАЗАЛ ВСЕМ FUCKING SLAVES И JABRONI НАДЕТЬ СВОИ BANDAGE И СДЕЛАТЬ ЕЙ FISTING ASS!!!")
    

@client.event
async def on_ready():
    print("Bot is ready")

def msgstatuser_turn():
    hr = datetime.datetime.now()
    hr2 = datetime.datetime(2021, 7, 5, 6, 00, 0)
    if (hr.hour == hr2.hour) and (hr.minute == hr2.minute):
       global  msgstatuser
       msgstatuser = "0"
    threading.Timer(10.0, msgstatuser_turn).start()
msgstatuser_thread = threading.Timer(10.0, msgstatuser_turn)
msgstatuser_thread.start()

client.run(Token)
