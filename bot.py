import discord
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

response_list = [
    'OAO',
    '我要出去浪了，誰管你🤣🤣🤣',
    '今天唱到喉嚨都沙啞了',
    '晚上吃龍蝦，開心',
    '我後天要去日本玩',
    '我明天要去蘭嶼玩',
    '我在逛街 OAO',
    '壞瓜瓜',
    '醫生叫我要早點睡',
    '我要睡了，掰掰掰掰掰'
]

@client.event
async def on_ready():
    print('目前登入身份：', client.user)
    game = discord.Game('浪到天涯海角')
    await client.change_presence(activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if random.random() <= 0.5:
        channel = message.channel
        await channel.send(random.choice(response_list))

client.run('MTE0MTczMDQzMDUwNTE5MzUzMg.GfwO3u.rBC6Kv4Sr1ey9tORDgrWsvCzqfzRdiNPuq3N28')
