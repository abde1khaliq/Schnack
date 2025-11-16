from django.contrib import admin
from .models import DiscordProfile, MessageHistory

@admin.register(DiscordProfile)
class DiscordProfileAdmin(admin.ModelAdmin):
    list_display = (
        'discord_user_id',
        'discord_username',
        'mother_language',
        'german_level',
        'target_level',
        'correction_style',
        'onboarding_complete',
        'created_at',
        'last_active_at',
    )
    list_filter = (
        'mother_language',
        'german_level',
        'target_level',
        'correction_style',
        'onboarding_complete',
    )
    search_fields = ('discord_user_id',)
    ordering = ('-last_active_at',)
    readonly_fields = ('created_at', 'last_active_at')

@admin.register(MessageHistory)
class MessageHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_message', 'schnack_response']