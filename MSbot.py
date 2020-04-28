import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("아직")
    game = discord.Game("베타테스트중")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("/안녕"):
        await message.channel.send("안녕하세요!")
    if message.content.startswith("/join")
        await message.channel.send("참가하려면 /summon 이라고 말해주세요!")
    if message.content.startswith("/엄준식")
        await message.channel.send("엄..")


client.run("NzA0MTM2NzQwMjYwMjgyNDQ5.XqaN3A.LbAZ7In9WeOdWfHZjJkGUm5PuMM")