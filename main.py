import requests
import discord
from discord.ext import commands
import random
from discord.ext.commands import has_permissions, MissingPermissions
import time
import re
import socket
import urllib
import urllib3
import web_server

client = discord.Client()
bot = commands.Bot(command_prefix = "-")


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Cowl Utility Bot!"))
    print("Ready to succ!")

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
headers = {
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
    'x-rapidapi-key': "KEY-GOES-HERE"
    }


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You are missing an argument(s).")
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("That command was not found.")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You are missing permissions to perform that command.")
    if isinstance(error, commands.MissingRole):
        await ctx.send("You are missing permissions to perform that command.")

@bot.command()
async def echo(ctx):
  message = (ctx.message.content)
  await ctx.send(message)

@bot.command(aliases=['define','def','Def','Define','DEF','DEFINE'])
async def _define(ctx, arg):


    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
    headers = {
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
        'x-rapidapi-key': "KEY-GOES-HERE"
    }

    querystring = {"term":  arg}

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    definition = response['list'][0]['definition']
    print(definition)

    await ctx.send(definition)

@bot.command(aliases=["short","shorturl"])
async def shortURL(ctx, arg):
    
    ToBeShort = (arg)

    key = "KEY-GOES-HERE"

    url = (f"https://cutt.ly/api/api.php?key={key}&short={arg}")

    response = requests.request("GET", url).json()

    short = response['url']['shortLink']

    print(short)

    await ctx.channel.purge(limit=1)

    await ctx.send(short)

@bot.command(aliases=["momma"])
async def mom(ctx):
    url = ("https://api.yomomma.info/")

    response = requests.request("GET", url).json()

    momjoke = response["joke"]

    print(momjoke)

    await ctx.send("`" + momjoke + "`")

@bot.command(aliases=['userid'])
async def id2user(ctx, userid:  int):
    user = bot.get_user(userid)
    await ctx.send(user.name)


@bot.command()
async def flip(ctx):
    coin = ["`Heads!`", "`Tails!`"]
    await ctx.send(random.choice(coin))

@bot.command()  
async def user2id(ctx, user: discord.Member):  
    await ctx.send(f"{user.mention}\'s id: `{user.id}`") 

@bot.command()
@commands.has_role("Staff")
async def f(ctx, amount : int):
    x = 1
    while True:
        await ctx.send("f")
        time.sleep(0.3)
        x += 1
        if x == amount + 1:
            break

@bot.command()
@commands.has_role("Staff")
async def purge(ctx, amount: int):
  amount = (amount + 1)
  deleted = await ctx.channel.purge(limit=amount)
  await ctx.send(f"Deleted {len(deleted)} messages")
  await asyncio.sleep(5)

@bot.command()
@commands.has_role("Staff")
async def spurge(ctx, amount: int):
  amount = (amount + 1)
  await ctx.channel.purge(limit=amount)

@bot.command()
@commands.has_role("Staff")
async def kick(ctx, member : discord.Member, *, arg):
    channel = await member.create_dm()
    await channel.send('You have been kicked for "' + arg + '"')
    await member.kick(reason = arg)
    await ctx.send("Kicked " + member.mention + " for " + arg)

@bot.command()
@commands.has_role("Staff")
async def ban(ctx, member : discord.Member, *, arg):
    channel = await member.create_dm()
    await channel.send('You have been banned for "' + arg + '"')
    await member.ban(reason = arg)
    await ctx.send("Banned " + member + " for " + arg)

@bot.command()
@commands.has_role("Staff")
async def unban(ctx, id: int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    await ctx.send(f'Unbanned {user.mention}')



@bot.command()
async def domain2ip(ctx, arg):
    domainName = (arg)
    ip = (socket.gethostbyname(domainName))
    await ctx.send("That domain's IP is:  " + ip)

@bot.command()
async def ip2geo(ctx, arg):

    ip = (arg)

    key = "KEY-GOES-HERE"

    url = ("http://api.ipstack.com/" + ip + "?access_key=" + key)

    querystring = {"format":"json"}

    headers = {
        'ip': "http://api.ipstack.com/" + ip,
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    country = response["country_name"]
    region = response["region_name"]
    city = response["city"]

    await ctx.send("That IP is located in:  " + city + ", " + region + ", " + country + ".")

@bot.command()
async def domain2geo(ctx, arg):
    domainName = (arg)
    ip = (socket.gethostbyname(domainName))
      
    domain = (ip)

    key = "KEY-GOES-HERE"

    url = ("http://api.ipstack.com/" + domain + "?access_key=" + key)

    querystring = {"format":"json"}

    headers = {
        'ip': "http://api.ipstack.com/" + domain,
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    country = response["country_name"]
    region = response["region_name"]
    city = response["city"]

    await ctx.send("That domain is located in:  " + city + ", " + region + ", " + country + ".")

@bot.command()
async def joke(ctx):

    url = "https://joke3.p.rapidapi.com/v1/joke"

    payload = "{ \"content\": \"A joke here\", \"nsfw\": \"false\"}"
    headers = {
        'x-rapidapi-host': "joke3.p.rapidapi.com",
        'x-rapidapi-key': "KEY-GOES-HERE",
        'content-type': "application/json",
        'accept': "application/json"
        }

    response = requests.request("GET", url, data=payload, headers=headers).json()

    joke = response["content"]
    print(joke)

    await ctx.send(f"`{joke}`")


@bot.command(aliases=["djoke"])
async def dad(ctx):
    
    headers = {'Accept' : 'application/json'}
    r = requests.get('https://icanhazdadjoke.com/', headers=headers).json()
    joke = r['joke']
    print(joke)
    await ctx.send(f"`{joke}`")

@bot.command(aliases=["8ball"])
async def spin(ctx, *, question):
    responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Definitely.", "You may rely on it.","As I see it, yes.", "Most likely.", "Outlook looks good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "It is better not to tell you, now.", "Cannot predict right now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.","My sources say no.", "Outlook is not so good.", "Very doubtful."]

    await ctx.send(f"Question:  {question}\nAnswer:  {random.choice(responses)}")

web_server.keep_alive()

bot.run("ENTER-TOKEN-HERE", bot = True, reconnect = True)
