import pygtail
import asyncio
import discord

token = "MTEwMDE2MjIyNjYyMDQ3MzQ4NA.G1vSmM.8oCkJU-KkgetM7BYXzBiAUtEBapwVOSwtkxgi4"
channel_id = 1100162737100836947  # Remove quotes to use an integer ID
log_file = "/home/eric/minecraft/logs/latest.log"

client = discord.Client()

async def send_logs():
    channel = client.get_channel(channel_id)
    while True:
        try:
            lines = pygtail.Pygtail(log_file)
            for line in lines:
                await channel.send(line)
        except FileNotFoundError:  # Move the except block outside the for loop
            pass
        await asyncio.sleep(1)

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
    await send_logs()

client.run(token)
