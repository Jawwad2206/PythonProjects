import responses
import discord


Token = "MTA5MzA3NTcxODc5MzA2ODYyNQ.GG9CHj.m_U05zV8ylD2aM3VeoaQEyzh3SDLs5fTZ0JGBM"


async def send_message(message, user_message, is_private):
    try:
        respnse = responses.get_response(user_message)
        await message.author.send(respnse) if is_private else await message.channel.send(respnse)

    except Exception as e:
        print(e)


def run_discord_bot():
    Token = "MTA5MzA3NTcxODc5MzA2ODYyNQ.GG9CHj.m_U05zV8ylD2aM3VeoaQEyzh3SDLs5fTZ0JGBM"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == "?":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(Token)



