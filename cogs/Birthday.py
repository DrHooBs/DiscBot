from ast import alias
from email import message
from discord.ext import commands
import discord
import discord.utils
import json
import os
from typing import Optional


a = {}



class Birthday(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='setBirthday', aliases=["setBday", "setbirthday"],brief="Stores your birthday in DAVE's database")
    async def set_Birthday(self, ctx, *, text: commands.clean_content = ''):
        #                         ^^ This is for pings - mentions being cleaned so you can't do `a!say @everyone`.
            # if "date:" not in text:
            #    await ctx.send("send your birthday like this: 'yyyy-mm-dd' if you don't want to share the year type '0000' as the year. Send this with the 'setBrithday' command (?setBirthday yyyy-mm-dd)")

            # elif "date:" in tex4t:
            
            if text == '':
                await ctx.send("send your birthday like this: 'yyyy-mm-dd' if you don't want to share the year type '0000' as the year. Send this with the 'setBrithday' command (?setBirthday yyyy-mm-dd)")
            elif text[4] != "-":
                await ctx.send("send your birthday like this: 'yyyy-mm-dd' if you don't want to share the year type '0000' as the year. Send this with the 'setBrithday' command (?setBirthday yyyy-mm-dd)")
            elif text[7] != "-":
                await ctx.send("send your birthday like this: 'yyyy-mm-dd' if you don't want to share the year type '0000' as the year. Send this with the 'setBrithday' command (?setBirthday yyyy-mm-dd)")
            #for number in range(5, 9):
            #    if text[number] != 
            #elif text[10] != ".":
            #   await ctx.send("send your birthday like this: 'yyyy-mm-dd.' if you don't want to share the year type '0000' as the year. Send this with the 'setBrithday' command (?setBirthday yyyy-mm-dd.)")

            else:

                    

                
                with open("user_info.json") as feedsjson: 
                    feeds = json.load(feedsjson)
                feeds[str(ctx.author.id)]['birthday'] = text.lower()
                for i in range(len(feeds)):
                    
                    with open("user_info.json", mode='w') as f:
                        f.write(json.dumps(feeds, indent=2)) 
                Birthday = feeds[str(ctx.author.id)]["birthday"] 
                await ctx.send(f"{ctx.author.name}'s birthday set to {Birthday}")



    



    @commands.command(name='Bday_check',aliases=["Bdaycheck", "bdaycheck", "bday_check"], description='informs you of the persons birthday',brief='informs you of a persons birthday: "?Bdaycheck @Strimis10"')
    async def say(self, ctx, target: Optional[discord.Member]):
        target = target or ctx.author
        with open("birthdays.json") as feedsjson: 
            feeds = json.load(feedsjson)
        name = target.name
        target_id = str(target.id)
        try:
            await ctx.send(f"{name}'s birthday is set to {feeds[target_id]}")
        
        except KeyError:
            await ctx.send(f"{name} has not set their birthday yet...")









def setup(bot):
    bot.add_cog(Birthday(bot))
    