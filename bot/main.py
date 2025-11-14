import discord
from decouple import config
from discord.ext import commands
from views import PrefrencesView
from embeds import PreferenceEmbed

GUILD_ID = discord.Object(id=1438445083824357469) if config(
    'DEVELOPMENT') == 'true' else None

intents = discord.Intents.default()
intents.message_content = True


class Lingual(commands.Bot):
    def __init__(self, command_prefix, *, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.seen_users = set()

    async def on_ready(self):
        print(f'Logged on as {self.user}')
        try:
            await self.tree.sync()
        except Exception as e:
            print(f'Error syncing commands: {e}')


client = Lingual(command_prefix="!", intents=intents)


@client.tree.command(name="settings", description="Set your preferred Lingual settings", guild=GUILD_ID)
async def language_setup(interaction: discord.Interaction):
    await interaction.response.send_message(embed=PreferenceEmbed, ephemeral=True, view=PrefrencesView())
    if interaction.guild == None:
        pass
    else:
        await interaction.followup.send(
            "📬 Want to continue enhancing your deutsch privately? Just DM me!", ephemeral=True)


client.run(config('LINGUAL_BOT_TOKEN'))
