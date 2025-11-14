from django.contrib import admin
from .models import DiscordProfile

@admin.register(DiscordProfile)
class DiscordProfileAdmin(admin.ModelAdmin):
    list_display = (
        'discord_user_id',
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