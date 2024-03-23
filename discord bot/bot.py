limport discord
from discord.ext import commands
import os
import asyncio
import json
import random

with open("data.json", "r") as f:
    data = json.load(f)

client = commands.Bot(command_prefix="d!", intents=discord.Intents.all(), application_id='1220710366514909294')

@client.event
async def on_ready():
    synced = await client.tree.sync()
    print(f"Bot is online. [Slash Commands Synced: {len(synced)}]")

    while not client.is_closed():
        with open("data.json", "w") as newf:
            json.dump(data, newf, indent=4)

        await asyncio.sleep(5)

# ------------COMMANDS------------

# stats
@client.hybrid_command(name="stats", description="Check your current stats.")
async def stats(interaction: discord.Interaction):
    author_id = interaction.message.author.id

    if not author_id in data:
        data[author_id] = {}
        data[author_id]["Coins"] = 0
        data[author_id]["Items"] = {}
    # determines if weapon in fight or no. if false, this means player owns the item, but doesnt use it in fight   

    embedmsg = discord.Embed(title="Your Stats", description=f"Coins: {data[author_id]["Coins"]}:coin:")
    await interaction.send(embed=embedmsg)

# ping
@client.hybrid_command(name="runspeed", description="Check bot's latency.")
async def runspeed(interaction: discord.Interaction):
    speed = round(client.latency * 1000)
    if speed >= 1500:
        await interaction.send(f"Responded in {speed} ms. (Bot is working too slowly? Report in our discord server in bot's description!)")
    else:
        await interaction.send(f"Responded in {speed} ms.")

# earn
@client.hybrid_command(name="earn", description="Find a 'normal' way to earn")
async def earn(interaction: discord.Interaction):
    author_id = interaction.message.author.id

    if not author_id in data:
        data[author_id] = {}
        data[author_id]["Coins"] = 0
        data[author_id]["Items"] = {}

    # determines if weapon in fight or no. if false, this means player owns the item, but doesnt use it in fight   
    amount=random.randint(-25, 30)
    random_response1 = [f"ok bud you worked enough, so u get paid {amount} bucks", f"good job, take your {amount} coins and get outta here", f"yoooo ur so cool, i wanna pay you {amount} bucks", f"why would u ever rob someone? but ig get your {amount}$", f"bro worked too much. but ig {amount} moneyz is yours"]
    random_response2 = [f"bro what did u do, im taking your {-amount} bucks for that", f"well ig you tried to rob someone but got arrested, u paid them {-amount} bucks", f"you racist im taking your {-amount} bucks"]
    data[author_id]["Coins"] += amount

    if amount >= 0:
        await interaction.send(random.choice(random_response1))
    else:
        await interaction.send(random.choice(random_response2))


# migrate (used to update slash commands)
@client.hybrid_command(name="migrate", description="Migrate to last update")
async def stats(interaction: discord.Interaction):
    await interaction.send("You're already migrated to last update!")
    
    

# ------------START UP------------
# i tried to make cogs but it doesnt work properly

client.run("deleted for safety")
