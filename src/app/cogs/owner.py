# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import json
import random
from app import exceptions as err
from app.utils import embed

class OwnerCog():
    def __init__(self, bot):
        self.bot = bot
    
    # Hidden means it won't show up on the default help.
    @commands.command(
        name='whoami', hidden=True,
        brief="Get the bot invite link",
        usage="`{0}whoami`"
    )
    @commands.is_owner()
    async def _whoami(self, ctx):
        """Return the bot invite link."""

        await ctx.message.author.send(f"https://discordapp.com/oauth2/authorize?" \
            f"client_id={self.bot._config['client_id']}&scope=bot&permissions=0")

    @commands.command(
        name='load', hidden=True,
        brief="Load a command module",
        usage="`{0}load [cog name]`"
    )
    @commands.is_owner()
    async def cog_load(self, ctx, *, cog: str):
        """Loads a command cog."""

        try:
            self.bot.load_extension(f'app.cogs.{cog}')
        except Exception as e:
            await ctx.send(embed=embed.error(description=f'**ERROR** - {type(e).__name__} - {e}'))
        else:
            await ctx.send(embed=embed.success(description='**SUCCESS**'))

    @commands.command(
        name='unload', hidden=True,
        brief="Unload a command module",
        usage="`{0}unload [cog name]`"
    )
    @commands.is_owner()
    async def cog_unload(self, ctx, *, cog: str):
        """Unloads a command cog."""

        try:
            self.bot.unload_extension(f'app.cogs.{cog}')
        except Exception as e:
            await ctx.send(embed=embed.error(description=f'**ERROR** - {type(e).__name__} - {e}'))
        else:
            await ctx.send(embed=embed.success(description='**SUCCESS**'))

    @commands.command(
        name='reload', hidden=True,
        brief="Reload a command module",
        usage="`{0}reload [cog name]`"
    )
    @commands.is_owner()
    async def cog_reload(self, ctx, *, cog: str):
        """Reloads a command cog."""

        try:
            self.bot.unload_extension(f'app.cogs.{cog}')
            self.bot.load_extension(f'app.cogs.{cog}')
        except Exception as e:
            await ctx.send(embed=embed.error(description=f'**ERROR** - {type(e).__name__} - {e}'))
        else:
            await ctx.send(embed=embed.success(description='**SUCCESS**'))

def setup(bot):
    bot.add_cog(OwnerCog(bot))
