import nextcord
from discord import Guild
from nextcord.ext import commands
from nextcord import application_command
import random
from nextcord.types.interactions import Interaction
import google.generativeai as genai
import requests
from google.generativeai.types import HarmCategory, HarmBlockThreshold, safety_types, palm_safety_types
import asyncio


percentage_chance = 0.069
percentage_chance_rare = 0.001 #not in use as of now
intents = nextcord.Intents.all()
add_reactions = True #check this out later
client = commands.Bot(command_prefix="&", intents=intents, activity=nextcord.Game(name='.hengus on discord')) #used for setting the 'playing' status


#saves the bot token as variable 'token'
with open('opToken', 'r') as f:
    discToken = f.read()

with open('GeminiAPIKey', 'r') as f:
    gemToken = f.read()

#prints this when the bot starts in console
@client.event
async def on_ready():
    print("The opposition is now ready to commence.")
    print("----------------------------------------")

@client.slash_command(name="hello", description="Say hello!")
async def hello(interaction: nextcord.Interaction):
    await interaction.response.send_message("Hello, world!")


#ping pong
@client.command()
async def order66(message):
    if 586286153368600576 == message.author.id:
        await message.channel.send("Pong")

#bans user
@client.command()
async def ban(message, member: nextcord.Member, *, reason=None):
    if 586286153368600576 == message.author.id:
        await member.ban(reason=reason)


#unbans user
@client.command(name='unban')
async def unban(message, id: int):
    user = await client.fetch_user(id)
    if 586286153368600576 == message.author.id:
        await message.guild.unban(user)

@client.command()
async def boom(message):
    if message.author.id == 586286153368600576:
        if message.author.voice:
            voice_channel = message.author.voice.channel
            voice = await voice_channel.connect()
            audio_source = nextcord.FFmpegPCMAudio(source="Metal20Pipes20Falling20Sound.mp3", executable="C:/FFmpeg/ffmpeg")
            audio_source = nextcord.PCMVolumeTransformer(audio_source, volume=2.0)  # DOUBLES the volume for the player
            voice.play(audio_source)
            await asyncio.sleep(2)
            await message.guild.voice_client.disconnect()
        else:
            await message.send("Cannot join if you are not in a VC BRUH")

@client.command()
async def peter(message):
    if message.author.id == 586286153368600576 or 449246777179111424:
        if message.author.voice:
            voice_channel = message.author.voice.channel
            voice = await voice_channel.connect()
            audio_source = nextcord.FFmpegPCMAudio(source="1319101682231017522.ogg", executable="C:/FFmpeg/ffmpeg")
            audio_source = nextcord.PCMVolumeTransformer(audio_source, volume=2.0)  # DOUBLES the volume for the player
            voice.play(audio_source)
            await asyncio.sleep(5)
            await message.guild.voice_client.disconnect()
        else:
            await message.send("Cannot join if you are not in a VC BRUH")

@client.command()
async def fork(message):
    if message.author.id == 586286153368600576:
        if message.author.voice:
            voice_channel = message.author.voice.channel
            voice = await voice_channel.connect()
            audio_source = nextcord.FFmpegPCMAudio(source="asmr.mp4", executable="C:/FFmpeg/ffmpeg")
            audio_source = nextcord.PCMVolumeTransformer(audio_source, volume=2.0)  # DOUBLES the volume for the player
            voice.play(audio_source)
            await asyncio.sleep(16)
            await message.guild.voice_client.disconnect()
        else:
            await message.send("Cannot join if you are not in a VC BRUH")

@client.command()
async def nuke(message):
    if message.author.id == 586286153368600576:
        if message.author.voice:
            voice_channel = message.author.voice.channel
            voice = await voice_channel.connect()
            audio_source = nextcord.FFmpegPCMAudio(source="even_more_rats.mp4", executable="C:/FFmpeg/ffmpeg")
            audio_source = nextcord.PCMVolumeTransformer(audio_source, volume=2.0)  # DOUBLES the volume for the player
            voice.play(audio_source)
            await asyncio.sleep(28)
            await message.guild.voice_client.disconnect()
        else:
            await message.send("Cannot join if you are not in a VC BRUH")

@client.command()
async def join(message):
    if message.author.voice:
        channel = message.author.voice.channel
        await channel.connect()
        await message.send("I joined VC")
    else:
        await message.send("Cannot join if you are not in a VC BRUH")

# @client.command()
# async def react(message: commands.Context):
#     msg = await message.send("This message will have reactions!")
#     await msg.add_reaction("👍")


@client.command()
async def leave(message):
    if message.voice_client:
        await message.guild.voice_client.disconnect()
        await message.send("I left VC")
    else:
        await message.send("I am not in a VC")



#add role
@client.command()
#@commands.has_permissions(manage_roles=True)
async def addrole(message, member: nextcord.Member, role: nextcord.Role):
    if 586286153368600576 == message.author.id:
        if role in member.roles:
            await message.send(f"{member.display_name} already has the role {role.name}.")
        else:
            await member.add_roles(role)
            await message.send(f"The role {role.name} has been added to {member.display_name}")



#remove roll
@client.command()
#@commands.has_permissions(manage_roles=True)
async def removerole(message, member: nextcord.Member, role: nextcord.Role):
    if 586286153368600576 == message.author.id:
        if role in member.roles:
            await member.remove_roles(role)
            await message.send(f"The role {role.name} has been removed from {member.display_name}")
        else:
            await message.send(f"{member.display_name} does not have the role {role.name}.")



#random gif post chance
@client.event
async def on_message(message):
    if random.random() < percentage_chance:
        if client.user.id != message.author.id:
            if 179780439450451968 == message.author.id: #sinon
                await message.channel.send("https://tenor.com/bR3U8.gif")
            elif 449246777179111424 == message.author.id:  # lee dragmire
                await message.channel.send("https://tenor.com/bS1da.gif")
            elif 1090427407145631854 == message.author.id:  # coded arrow
                await message.channel.send("https://tenor.com/bRaFA.gif")
            elif 776273258948460544 == message.author.id:  # boykisser
                await message.channel.send("https://tenor.com/g1NToY7Pq81.gif")
            elif 658135980297158659 == message.author.id:  # archen444
                await message.channel.send("https://tenor.com/d4XrdvpAIn.gif")
            elif 586286153368600576 == message.author.id:  # hengus
                await message.channel.send("https://tenor.com/bViXP.gif")
            elif 409525708491063306 == message.author.id:  # trashcan - lillery
                await message.channel.send("https://tenor.com/b04Z6.gif")
        pass
    else:
        pass

    # watch for a specific message sent, then type something in response
    # can be BRUTALLY exploited, please fix below code snippet later : )
    
    # if "you" and "should" and "watch" in message.content.casefold():
    #     await message.channel.send("No")
    #     pass
    # else:
    #     pass


    #used for displaying available roles for a server
    #print(message.guild.roles)

# this works, it will annoy
#     if 586286153368600576 == message.author.id: #hengus
#         await message.add_reaction("👍")
#     elif 658135980297158659 == message.author.id: #archen
#         await message.add_reaction("🤓")
#     await client.process_commands(message)

    # this works, it will annoy
    # if 776273258948460544 == message.author.id: #boykiss
    #     await message.add_reaction("💋")

    await client.process_commands(message)

@client.command()
async def ai(message):
    genai.configure(api_key=gemToken)

    #Don't believe code in curly braces actually called, fix later : )
    generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 40,
      "max_output_tokens": 500,
      "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    system_instruction="You are a very rude and mean person. An opposition.",
    )

    chat_session = model.start_chat(
      history=[
      ]
    )

    #I know its terrible, bear me the shame...
    response = chat_session.send_message(message.message.content)

    await message.channel.send(response.text)


#runs bot with 'token' var
if __name__ == "__main__":
    client.run(discToken)

'''

Things to do:

Add to GitHub ✅ 
Claim dev badge ✅ 
Add file that can be used to append with dict to see how many times a person has been sent a gif 
Implement ai for trolling because im a ai FIEND ig ✅ 
Implement sustaining chat history on the gemini AI
Remove safety filters on the gemini AI *extra trolling* 
See if there are limited chat tokens on the gemini AI 
Look into training ai model from discord server | scraping

'''