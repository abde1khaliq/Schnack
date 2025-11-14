import discord


class MotherLanguageDropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label='Arabic', value='ar'),
            discord.SelectOption(label='English', value='en'),
            discord.SelectOption(label='Spanish', value='es'),
            discord.SelectOption(label='French', value='fr'),
            discord.SelectOption(label='German', value='de'),
            discord.SelectOption(label='Turkish', value='tr'),
            discord.SelectOption(label='Russian', value='ru'),
            discord.SelectOption(label='Hindi', value='hi'),
            discord.SelectOption(label='Chinese (Mandarin)', value='zh'),
            discord.SelectOption(label='Japanese', value='ja'),
            discord.SelectOption(label='Korean', value='ko'),
            discord.SelectOption(label='Portuguese', value='pt'),
            discord.SelectOption(label='Italian', value='it'),
            discord.SelectOption(label='Dutch', value='nl'),
            discord.SelectOption(label='Swahili', value='sw'),
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
            discord.SelectOption(label='German', value='de', default=True),
        ]
        super().__init__(
            placeholder="Select the language you want to learn",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        # Soon going to implement the actual language set logic.
        pass
