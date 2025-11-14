from django.db import models


class DiscordProfile(models.Model):
    GERMAN_LEVELS = [
        ("none", "I don't know anything", "Start with basic greetings and alphabet."),
        ("A1", "A1 - Beginner", "Focus on simple sentences and common verbs."),
        ("A2", "A2 - Elementary", "Introduce past tense and everyday vocabulary."),
        ("B1", "B1 - Intermediate", "Practice conversations and grammar nuances."),
        ("B2", "B2 - Upper Intermediate", "Refine fluency and handle abstract topics."),
        ("C1", "C1 - Advanced", "Work on precision, idioms, and native-like flow."),
        ("C2", "C2 - Mastery / Near-native", "Challenge with native-level texts and debates."),
    ]

    MOTHER_LANGUAGES = [
        ("Arabic", "ar"),
        ("English", "en"),
        ("Spanish", "es"),
        ("French", "fr"),
        ("German", "de"),
        ("Turkish", "tr"),
        ("Russian", "ru"),
        ("Hindi", "hi"),
        ("Chinese (Mandarin)", "zh"),
        ("Japanese", "ja"),
        ("Korean", "ko"),
        ("Portuguese", "pt"),
        ("Italian", "it"),
        ("Dutch", "nl"),
        ("Swahili", "sw"),
    ]

    TARGET_LEVELS = [
        ("A1", "A1 - Beginner"),
        ("A2", "A2 - Elementary"),
        ("B1", "B1 - Intermediate"),
        ("B2", "B2 - Upper Intermediate"),
        ("C1", "C1 - Advanced"),
        ("C2", "C2 - Mastery / Near-native"),
    ]

    CORRECTION_STYLES = [
        ("gentle", "Gentle"),
        ("direct", "Direct"),
        ("explanatory", "Explanatory"),
        ("minimal", "Minimal"),
        ("native-like", "Native"),
    ]

    discord_user_id = models.BigIntegerField(
        primary_key=True, max_length=18, unique=True)
    mother_language = models.CharField(max_length=50, choices=MOTHER_LANGUAGES)
    german_level = models.CharField(max_length=50, choices=[(
        label, value) for label, value, _ in GERMAN_LEVELS], default="none")
    target_level = models.CharField(max_length=50, choices=TARGET_LEVELS)
    correction_style = models.CharField(
        max_length=50, choices=CORRECTION_STYLES)
    onboarding_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_active_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User {self.discord_user_id}"
