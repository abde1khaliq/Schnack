from django.db import models


class DiscordProfile(models.Model):
    GERMAN_LEVELS = [
        ("I know nothing - Start with basic greetings and alphabet.", "none"),
        ("A1 - Focus on simple sentences and common verbs.", "a1"),
        ("A2 - Introduce past tense and everyday vocabulary.", "a2"),
        ("B1 - Practice conversations and grammar nuances.", "b1"),
        ("B2 - Refine fluency and handle abstract topics.", "b2"),
        ("C1 - Work on precision, idioms, and native-like flow.", "c1"),
        ("C2 - Challenge with native-level texts and debates.", "c2"),
    ]

    MOTHER_LANGUAGES = [
        ("Arabic", "arabic"),
        ("English", "english"),
        ("Spanish", "spanish"),
        ("French", "french"),
        ("German", "german"),
        ("Turkish", "turkish"),
        ("Russian", "russian"),
        ("Hindi", "hindi"),
        ("Chinese (Mandarin)", "chinese (mandarin)"),
        ("Japanese", "japanese"),
        ("Korean", "korean"),
        ("Portuguese", "portuguese"),
        ("Italian", "italian"),
        ("Dutch", "dutch"),
        ("Swahili", "swahili"),
    ]

    TARGET_LEVELS = [
        ("A1 - Beginner", "a1"),
        ("A2 - Elementary", "a2"),
        ("B1 - Intermediate", "b1"),
        ("B2 - Upper Intermediate", "b2"),
        ("C1 - Advanced", "c1"),
        ("C2 - Mastery / Near-native", "c2"),
    ]

    CORRECTION_STYLES = [
        ("Gentle", "gentle"),
        ("Direct", "direct"),
        ("Explanatory", "explanatory"),
        ("Minimal", "minimal"),
    ]

    discord_user_id = models.IntegerField(
        primary_key=True, unique=True)
    discord_username = models.CharField(null=True, blank=True)
    mother_language = models.CharField(max_length=50, choices=MOTHER_LANGUAGES)
    german_level = models.CharField(max_length=100, choices=GERMAN_LEVELS)
    target_level = models.CharField(max_length=50, choices=TARGET_LEVELS)
    correction_style = models.CharField(
        max_length=50, choices=CORRECTION_STYLES)
    onboarding_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_active_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User {self.discord_user_id}"
