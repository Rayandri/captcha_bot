import discord
import json
from discord.ext import commands
from captchagenerator import generate, random_image, image

NB_IMAGE = 10000
TIMEOUT = 60

generate(NB_IMAGE)

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot("-", intents = intents)

bot.remove_command("help") # To create a personal help command 

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    print(discord.__version__)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"?help"))


@bot.event
async def on_member_join(member):


    image, answer = random_image(NB_IMAGE)
    embed=discord.Embed(title="Please verify yourself to gain access to the CLUBMETAHOUSE discord server.", description="**NOTE:** The captcha is CaSe SenSiTivE and does not include spaces.", color=0x1997e6)
    file = discord.File(image, filename="captcha.png")
    embed.set_image(url="attachment://captcha.png")
    embed.add_field(name="Please send the captcha below in this DM.", value="‎", inline=True)
    initial = await member.send(file=file, embed=embed)

    channel = member.dm_channel

    def check(message):
        return message.channel == channel

    
    stop = False
    while not stop :
        
        try :
            msg = (await bot.wait_for("message", check=check, timeout=TIMEOUT)).content
        except :
            await member.guild.kick(member)
            await initial.edit(suppress=True, content="Timed out, please retry with : https://discord.gg/d4eP66VYfZ")
        else:
            if msg != answer :
                image, answer = random_image(NB_IMAGE)
                embed=discord.Embed(title="Wrong ! Please try again.", description="**NOTE:** The captcha is CaSe SenSiTivE and does not include spaces.", color=0x1997e6)
                file = discord.File(image, filename="captcha.png")
                embed.set_image(url="attachment://captcha.png")
                embed.add_field(name="Please send the captcha below in this DM.", value="‎", inline=True)
                await member.send(file=file, embed=embed)
            elif msg == answer :
                stop = True


    await member.send("Success ! You passed the verification successfully")
    role = discord.utils.get(member.guild.roles, id=971441991328084018)
    await member.add_roles(role)

@bot.command(name = 'test')
async def test(ctx):
    image, answer = random_image()
    await ctx.send(file=discord.File(image))
    await ctx.send(f"||{answer}||")

@bot.command(name="embed")
async def embed(ctx) :
    embed=discord.Embed(title="Please verify yourself to gain access to the CLUBMETAHOUSE discord server.", description="**NOTE:** The captcha is CaSe SenSiTivE and does not include spaces.", color=0x1997e6)
    file = discord.File("dataimage/png/1.png", filename="captcha.png")
    embed.set_image(url="attachment://captcha.png")
    embed.add_field(name="Please send the captcha below in this DM.", value="‎", inline=True)
    await ctx.send(file=file, embed=embed)


with open("config.json", "r") as config:
    data = json.load(config)
    token = data["token"]
bot.run(token) 