import time

import discord
from discord.ext import tasks
from decouple import config
import main
token=config('DISCORD_TOKEN')

class Bot(discord.Client):
    async def on_ready(self):
        channel_updater.start()
        print('Logged on as', self.user)


@tasks.loop(minutes=60)
async def channel_updater():
    print("Updating channels")
    original, radiated, radiated2, pharos = main.get_price()

    channel = await client.fetch_channel(1072548291348279417)
    time.sleep(10)

    await channel.edit(name=f"DegenBoyz: ◎{original}")
    time.sleep(10)

    channel = await client.fetch_channel(1072601477673132172)
    await channel.edit(name=f"RadiatedBoyzT1: ◎{radiated}")
    time.sleep(10)

    channel = await client.fetch_channel(1072599322694271016)
    await channel.edit(name=f"RadiatedBoyzT2: ◎{radiated2}")
    time.sleep(10)

    channel = await client.fetch_channel(1072602555261132952)
    await channel.edit(name=f"DegenPharaohz: ◎{pharos}")
    time.sleep(10)

    solPrice = main.get_sol()

    channel = await client.fetch_channel(1072609878163599440)
    await channel.edit(name=f"SolanaPrice: ${solPrice}")

    print("Channels name updated")

#intents.message_content = True
intents = discord.Intents.default()

client = Bot(intents=intents)
client.run(token)
