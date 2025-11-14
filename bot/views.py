import discord
from ui import MotherLanguagesDropdown, CorrectionStylesDropdown, TargetLevelsDropdown, GermanLevelsDropdown
from backend_requests import get_correction_style_options, get_mother_language_options, get_target_level_options, get_german_level_options

class PrefrencesView(discord.ui.View):
    def __init__(self, mother_language_options, correction_style_options, target_level_options, german_level_options):
        super().__init__()
        self.add_item(MotherLanguagesDropdown(mother_language_options))
        self.add_item(GermanLevelsDropdown(german_level_options))
        self.add_item(TargetLevelsDropdown(target_level_options))
        self.add_item(CorrectionStylesDropdown(correction_style_options))

    @classmethod
    async def create(cls):
        mother_language_options = await get_mother_language_options()
        correction_style_options = await get_correction_style_options()
        target_level_options = await get_target_level_options()
        german_level_options = await get_german_level_options()
        return cls(mother_language_options, correction_style_options, target_level_options, german_level_options)