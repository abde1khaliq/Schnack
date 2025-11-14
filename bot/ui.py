import discord

class MotherLanguagesDropdown(discord.ui.Select):
    def __init__(self, options):
        super().__init__(
            placeholder="🌍 Choose your native (mother) language",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        selected = self.values[0]
        await interaction.response.send_message(
            f"✅ Your native language has been set to **{selected}**.",
            ephemeral=True
        )

class CorrectionStylesDropdown(discord.ui.Select):
    def __init__(self, options):
        super().__init__(
            placeholder="🛠️ Choose your preferred correction style",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        selected = self.values[0]
        await interaction.response.send_message(
            f"✅ Correction style set to **{selected}**. We'll tailor feedback accordingly.",
            ephemeral=True
        )

class TargetLevelsDropdown(discord.ui.Select):
    def __init__(self, options):
        super().__init__(
            placeholder="🎯 Select the German level you aim to reach",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        selected = self.values[0]
        await interaction.response.send_message(
            f"✅ Your target German level is now set to **{selected}**.",
            ephemeral=True
        )

class GermanLevelsDropdown(discord.ui.Select):
    def __init__(self, options):
        super().__init__(
            placeholder="📚 Select your current German proficiency level",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        selected = self.values[0]
        await interaction.response.send_message(
            f"✅ Your current German level is set to **{selected}**.",
            ephemeral=True
        )