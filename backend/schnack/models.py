from django.db import models


class Discord_Profile(models.Model):
    GERMAN_LEVELS = [
        ("I don't know anything", "none", "Start with basic greetings and alphabet."),
        ("A1 - Beginner", "A1", "Focus on simple sentences and common verbs."),
        ("A2 - Elementary", "A2", "Introduce past tense and everyday vocabulary."),
        ("B1 - Intermediate", "B1", "Practice conversations and grammar nuances."),
        ("B2 - Upper Intermediate", "B2",
         "Refine fluency and handle abstract topics."),
        ("C1 - Advanced", "C1", "Work on precision, idioms, and native-like flow."),
        ("C2 - Mastery / Near-native", "C2",
         "Challenge with native-level texts and debates."),
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
        ("A1 - Beginner", "A1"),
        ("A2 - Elementary", "A2"),
        ("B1 - Intermediate", "B1"),
        ("B2 - Upper Intermediate", "B2"),
        ("C1 - Advanced", "C1"),
        ("C2 - Mastery / Near-native", "C2"),
    ]

    CORRECTION_STYLES = [
        ("Gentle", "gentle"),
        ("Direct", "direct"),
        ("Explanatory", "explanatory"),
        ("Minimal", "minimal"),
        ("Native-like", "native"),
    ]

    discord_user_id = models.BigIntegerField(primary_key=True)
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
