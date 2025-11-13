import discord
from ui import MotherLanguageDropdown, LearningLanguageDropdown


class PrefrencesView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(MotherLanguageDropdown())
        self.add_item(LearningLanguageDropdown())