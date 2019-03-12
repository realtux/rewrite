import random
from pathlib import Path

from discord import Colour, Embed
from discord.ext.commands import Cog, command

paths = {
    "bond": Path('resources') / 'bonds.txt',  # list of bonds
    "flaw": Path('resources') / 'flaws.txt',  # list of flaws
    "ideal": Path('resources') / 'ideals.txt',  # list of ideals
    "trait": Path('resources') / 'traits.txt',  # list of traits
}


class GeneratorCog(Cog, name='Generator'):

    def __init__(self, bot):
        self.bot = bot

    @command(name='generate')
    async def generator_command(self, ctx, generate_num=None):
        """All of the generate commands that are used to generate things, such as:
        characters, npc's and names."""
        generator_embed = Embed(colour=Colour.blurple())
        commands = ['bond', 'flaw', 'ideal', 'trait']
        desc = ''
        num = 0
        if generate_num is None:
            generator_embed.title = 'All of the Generator Commands'
            for _ in commands:
                desc += f'**{commands[num]}** \n'
                num = num + 1
            generator_embed.description = desc
            generator_embed.set_footer(text='Use ;generate {command} to use one of the above commands.')
            return await ctx.send(embed=generator_embed)
        final = str.casefold(generate_num)
        with open(paths[final], 'r') as f:
            strings = f.readlines()
        return await ctx.send(random.choice(strings))


def setup(bot):
    bot.add_cog(GeneratorCog(bot))