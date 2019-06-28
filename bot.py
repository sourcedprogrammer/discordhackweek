import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    print('Bot is ready!')

@client.event
async def on_member_join(ctx, member):
    print(f'{member} has joined {ctx.guild.name}.')

@client.event
async def on_member_remove(ctx, member):
    print(f'{member} has left {ctx.guild.name}.')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name="Member")
    await client.add_roles(member, role)

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! :ping_pong: **{round(client.latency * 1000)}ms** ')

@client.command()
async def purge(ctx, amount=5):
    await ctx.channel.delete(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
async def pardon(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.banned_users

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)

client.run('NTkzNjA5MjEwNzk3NzUyMzMz.XRQYhw.wSwylwG8RAA4xK2eobsBXGkmhT4')
