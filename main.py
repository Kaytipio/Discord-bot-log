import discord
from discord.ext import commands
import datetime
import discord.ui
from discord.ui import View, Button, Select


bot = commands.Bot(command_prefix=".", intents=discord.Intents.all(), status=discord.Status.online)


@bot.event
async def on_ready():
    print(f"{bot.user} logged")

modlog_channel_id = CHANNEL ID

@bot.event
async def on_member_ban(guild, user):
    modlog_channel = guild.get_channel(modlog_channel_id)
    if modlog_channel:
        await modlog_channel.send(f'{user.name}#{user.discriminator} has been banned.')

@bot.event
async def on_member_unban(guild, user):
    modlog_channel = guild.get_channel(modlog_channel_id)
    if modlog_channel:
        await modlog_channel.send(f'{user.name}#{user.discriminator} has been unbanned.')

@bot.event
async def on_member_remove(member):
    modlog_channel = member.guild.get_channel(modlog_channel_id)
    if modlog_channel:
        await modlog_channel.send(f'{member.name}#{member.discriminator} has been kicked.')

@bot.event
async def on_message_delete(message):
    modlog_channel = message.guild.get_channel(modlog_channel_id)
    if modlog_channel:
        await modlog_channel.send(f'Message from {message.author.name}#{message.author.discriminator} deleted: {message.content}')

@bot.event
async def on_message_edit(before, after):
    modlog_channel = before.guild.get_channel(modlog_channel_id)
    if modlog_channel:
        await modlog_channel.send(f'Message from {before.author.name}#{before.author.discriminator} edited: \nBefore: {before.content} \nAfter: {after.content}')

@bot.event
async def on_guild_role_create(role):
    modlog_channel = role.guild.get_channel(modlog_channel_id)
    if modlog_channel:
        await modlog_channel.send(f'Role {role.name} created.')

@bot.event
async def on_guild_role_delete(role):
    modlog_channel = role.guild.get_channel(modlog_channel_id)
    if modlog_channel:
        await modlog_channel.send(f'Role {role.name} deleted.')

@bot.event
async def on_guild_role_update(before, after):
    modlog_channel = before.guild.get_channel(modlog_channel_id)
    if modlog_channel:
        if before.name != after.name:
            await modlog_channel.send(f'Role {before.name} renamed to {after.name}.')
        if before.permissions != after.permissions:
            await modlog_channel.send(f'Permissions for role {before.name} updated.')


bot.run("Your token here")
