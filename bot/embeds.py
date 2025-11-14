import discord

PreferenceEmbed = discord.Embed(
    title="Let's Get You Set Up!",
    description=(
        "**Welcome to Schnack!**\n\n"
        "To personalize your experience, please select the following preferences:\n\n"
        "🔸 **Mother Language** — This helps Schnack understand your background and tailor explanations in a way that makes sense to you.\n"
        "🔸 **Current German Level** — Choose the level you're currently at so feedback matches your skill.\n"
        "🔸 **Target German Level** — Set your goal so Schnack can help you progress toward it.\n"
        "🔸 **Correction Style** — Pick how you'd like mistakes to be corrected: gently, directly, or with explanations.\n\n"
        "These settings help Schnack deliver smarter, more supportive feedback as you learn. You can update them anytime!"
    ),
    color=int('f26522', 16)
)
