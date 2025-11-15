import discord
from backend_requests import save_user_preference_to_backend


class MotherLanguagesDropdown(discord.ui.Select):
    def __init__(self, options):
        super().__init__(
            placeholder="🌍 Choose your native (mother) language",
            min_values=1,
            max_values=1,
            options=options,
            custom_id="mother_language_dropdown"
        )

    async def callback(self, interaction: discord.Interaction):
        try:
            interaction.client.user_preferences[interaction.user.id]["mother_language"] = self.values[0]
            await interaction.response.defer(ephemeral=True)
            print(
                f"{interaction.user.id} set mother_language to {self.values[0]}")
        except Exception as e:
            print(f"Error in MotherLanguagesDropdown callback: {e}")
            await interaction.response.send_message("⚠️ Something went wrong saving your selection.", ephemeral=True)


class CorrectionStylesDropdown(discord.ui.Select):
    def __init__(self, options):
        super().__init__(
            placeholder="🛠️ Choose your preferred correction style",
            min_values=1,
            max_values=1,
            options=options,
            custom_id="correction_styles_dropdown"
        )

    async def callback(self, interaction: discord.Interaction):
        try:
            interaction.client.user_preferences[interaction.user.id]["correction_style"] = self.values[0]
            await interaction.response.defer(ephemeral=True)

            print(
                f"{interaction.user.id} set correction_style to {self.values[0]}")
        except Exception as e:
            print(f"Error in CorrectionStylesDropdown callback: {e}")
            await interaction.response.send_message("⚠️ Something went wrong saving your selection.", ephemeral=True)


class TargetLevelsDropdown(discord.ui.Select):
    def __init__(self, options):
        super().__init__(
            placeholder="🎯 Select the German level you aim to reach",
            min_values=1,
            max_values=1,
            options=options,
            custom_id="target_levels_dropdown"
        )

    async def callback(self, interaction: discord.Interaction):
        try:
            interaction.client.user_preferences[interaction.user.id]["target_level"] = self.values[0]
            await interaction.response.defer(ephemeral=True)

            print(
                f"{interaction.user.id} set target_level to {self.values[0]}")
        except Exception as e:
            print(f"Error in TargetLevelsDropdown callback: {e}")
            await interaction.response.send_message("⚠️ Something went wrong saving your selection.", ephemeral=True)


class GermanLevelsDropdown(discord.ui.Select):
    def __init__(self, options):
        super().__init__(
            placeholder="📚 Select your current German proficiency level",
            min_values=1,
            max_values=1,
            options=options,
            custom_id="german_levels_dropdown"
        )

    async def callback(self, interaction: discord.Interaction):
        try:
            interaction.client.user_preferences[interaction.user.id]["german_level"] = self.values[0]
            await interaction.response.defer(ephemeral=True)

            print(
                f"{interaction.user.id} set german_level to {self.values[0]}")
        except Exception as e:
            print(f"Error in GermanLevelsDropdown callback: {e}")
            await interaction.response.send_message("⚠️ Something went wrong saving your selection.", ephemeral=True)


class UserPreferenceSubmitButton(discord.ui.Button):
    def __init__(self):
        super().__init__(label='Save Preferences', style=discord.ButtonStyle.success)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)

        preferences = interaction.client.user_preferences.get(
            interaction.user.id, {})

        payload = {
            "discord_user_id": interaction.user.id,
            "discord_username": interaction.user.global_name,
            **preferences,
            "onboarding_complete": True
        }

        response = await save_user_preference_to_backend(payload)

        if response[0] == 201:
            await interaction.followup.send("I've saved your preferences successfully. Wohoo! 😎", ephemeral=True)
        elif response[0] == 400:
            error_lines = [
                f'🔸 **{field.capitalize()}**: {message[0].capitalize()}'
                for field, message in response[1].items()
            ]
            await interaction.followup.send("\n".join(error_lines), ephemeral=True)
        else:
            await interaction.followup.send("⚠️ Unexpected error occurred. Please try again later.", ephemeral=True)
