import discord


class MotherLanguageDropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label='Arabic', value='ar'),
            discord.SelectOption(label='English', value='en'),
        ]
        super().__init__(
            placeholder="Select your mother language",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        # Soon going to implement the actual language set logic.
        pass


class LearningLanguageDropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label='Deutsch', value='de'),
        ]
        super().__init__(
            placeholder="Select the language you want to learn",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        # Soon going to implement the actual language set logic.
        pass