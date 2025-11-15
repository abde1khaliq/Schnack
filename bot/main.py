import discord
from decouple import config
from discord.ext import commands
from views import PrefrencesView
from embeds import PreferenceEmbed
from collections import defaultdict
from backend_requests import check_if_user_exists

GUILD_ID = discord.Object(id=1438445083824357469) if config(
    'DEVELOPMENT') == 'true' else None

intents = discord.Intents.default()
intents.message_content = True


class Schnack(commands.Bot):
    def __init__(self, command_prefix, *, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)

    async def on_ready(self):
        print(f'Logged on as {self.user}')
        try:
            await self.tree.sync()
        except Exception as e:
            print(f'Error syncing commands: {e}')


client = Schnack(command_prefix="!", intents=intents)
client.user_preferences = defaultdict(dict)


@client.tree.command(name="setup", description="Set up your Schnack bot based on your preferences.", guild=GUILD_ID)
async def setup(interaction: discord.Interaction):
    user_checker = await check_if_user_exists(interaction.user.id)
    if user_checker == 200:
        await interaction.response.send_message('You have already set your preferences. use `/update-preferences` to update them.')
    else:
        view = await PrefrencesView.create()
        await interaction.response.send_message(embed=PreferenceEmbed, ephemeral=True, view=view)
        if interaction.guild:
            await interaction.followup.send(
                "📬 Want to continue learning german? Just DM me!", ephemeral=True)

client.run(config('SCHNACK_BOT_TOKEN'))
