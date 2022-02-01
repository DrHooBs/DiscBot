##https://www.youtube.com/watch?v=k6eCJDSemu4

from datetime import datetime
from sqlite3 import Timestamp
from typing import Optional
from ast import alias
from discord.ext import commands
import discord
import discord.utils
import random








class userInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='User_info', aliases=["ui", "Memeber_info", "mi"],description='gives a summary of the user')
    async def user_info(self, ctx, target: Optional[discord.Member]):
        target = target or ctx.author

        embed = discord.Embed(title="User information",
                                    colour=target.colour,
                                    Timestamp=datetime.utcnow())

        fields = [("ID", target.id, False),
                ("Username", str(target), True,),
                ("Bot?", target.bot, True),
                ("Server Booster", bool(target.premium_since), True),  
                ("Top role", target.top_role.mention, True),
                #("Status", str(target.status).title(), True),
                # ("Activity", f"{target.activity.name} {str(getattr(target.activity, 'type')).title()}", True)
                ("Is Admin", bool(target.guild_permissions.administrator), True),
                ("Created at", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), False),
                ("Joined at", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), True),
                
                
                ]

        for name, value, inline in fields: 
            embed.add_field(name=name, value=value, inline=inline)       
            embed.set_thumbnail(url=target.avatar_url)
        await ctx.send(embed=embed)


    @commands.command(name='Server_info', aliases=["si"])
    async def server_info(self, ctx):
        pass

    @commands.command(name='JamesSus',description='sus')
    async def susJames(self, ctx):
        file = discord.File("pokemon.gif")
        await ctx.send(file=file)



    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.lower().startswith("try again"):
            if message.author.id != 932687176997687316:
                await message.reply("*Kenny making a funny face;  EEVEE: Constipated")



def setup(bot):
    bot.add_cog(userInfo(bot))




