import discord
from decouple import config
from discord.ext import commands
from views import PrefrencesView
from embeds import PreferenceEmbed
from collections import defaultdict
from backend_requests import check_if_user_exists, respond_to_user, save_user_history

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

    async def on_message(self, message):
        if message.author.bot:
            return

        user_checker = await check_if_user_exists(message.author.id)
        if user_checker == 200:
            if message.guild is None:
                user_id = message.author.id
                self.user_history[user_id]["user_message"] = message.content
                try:
                    async with message.channel.typing():
                        response = await respond_to_user(message.author.id, message.content)
                    if response:
                        await message.channel.send(response['response'])
                        self.user_history[user_id]["schnack_response"] = response["response"]
                        await save_user_history(user_id=user_id, user_message=self.user_history[user_id]["user_message"], schnack_response=self.user_history[user_id]["schnack_response"])
                    else:
                        await message.channel.send("Sorry, I couldn't generate a response.")
                except Exception as error:
                    print(
                        f"⚠️ Error responding to user {message.author.id}: {error}")
                    await message.channel.send("Something went wrong while processing your message. ")
        elif user_checker == 404:
            try:
                await message.channel.send(f"Hey {message.author.display_name}, Make sure to setup your preferences using `/setup` so I can personalize your experience!")
            except Exception as error:
                print('An error occured notifying the user to set up their preferences')
        else:
            try:
                await message.channel.send(f"Hey {message.author.display_name}, I'm having trouble responding at the moment. Try again later")
            except Exception as error:
                print('An error occured notifying the user to set up their preferences')


client = Schnack(command_prefix="!", intents=intents)
client.user_preferences = defaultdict(dict)
client.user_history = defaultdict(
    lambda: {"user_message": None, "schnack_response": None})


@client.tree.command(name="setup", description="Set up your Schnack bot based on your preferences.", guild=GUILD_ID)
async def setup(interaction: discord.Interaction):
    user_checker = await check_if_user_exists(interaction.user.id)

    if user_checker == 200:
        await interaction.response.send_message(
            'You have already set your preferences. Use `/update-preferences` to update them.',
            ephemeral=True
        )
        return

    try:
        await interaction.response.defer(ephemeral=True)  # Gives you more time
        view = await PrefrencesView.create()
        await interaction.followup.send(embed=PreferenceEmbed, view=view)
        if interaction.guild:
            await interaction.followup.send(
                "📬 Want to continue learning German? Just DM me!",
                ephemeral=True
            )
    except Exception as error:
        print(f"⚠️ Setup command failed: {error}")
        await interaction.followup.send(
            "Something went wrong while setting up your preferences.",
            ephemeral=True
        )

client.run(config('SCHNACK_BOT_TOKEN'))
