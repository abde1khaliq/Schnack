from google import genai
from decouple import config
import json


class GeminiEngine:
    def __init__(self):
        try:
            api_key = config("GEMINI_API_KEY")
            self.client = genai.Client(api_key=api_key)
            self.model = "gemini-2.5-flash-lite"
        except Exception as error:
            print(f"⚠️ Error initializing Gemini client: {error}")
            self.client = None

    def format_history(self, history: list[dict]) -> str:
        """
        Converts a list of message history dicts into a readable dialogue format.
        """
        return "\n".join(
            f"User: {msg['user_message']}\nSchnack: {msg['schnack_response']}"
            for msg in history if msg['user_message'] or msg['schnack_response']
        )

    def build_prompt(
        self,
        discord_user_id: int,
        username: str,
        user_german_level: str,
        user_mother_language: str,
        user_target_level: str,
        user_correction_style: str,
        user_input: str,
        formatted_history: str
    ) -> str:
        prompt = f"""
        You are a casual German-speaking friend named Schnack chatting with {username} (userId: {discord_user_id} — do not mention this).

        🎯 Your mission:
        - Respond ONLY in German.
        - Keep replies short, direct, and conversational — maximum 1–2 sentences.
        - Correct mistakes briefly using Discord markdown (**bold**, *italic*, `inline code`).
        - Do not explain grammar or vocabulary unless the user explicitly asks.
        - Do not add emojis, filler phrases, or rhetorical questions.
        - Do not start with greetings like "Hallo" or "Hey" unless the user greets you first.
        - Never ask "Verstehst du?" or similar — just respond naturally.

        🧠 User profile:
        - German Level: {user_german_level}
        - Target Level: {user_target_level}
        - Mother Language: {user_mother_language}
        - Correction Style: {user_correction_style}

        💬 Conversation so far:
        {formatted_history}

        🆕 Latest user message:
        User: {user_input}

        ⚡ Response rules:
        - Respond directly to the latest user message in 1–2 concise lines.
        - If correction is needed, apply it inline and continue naturally.
        - Keep tone playful and natural, but avoid unnecessary detail.
        - Your output must be short, clear, and to the point.
        Schnack:"""

        return prompt

    def get_response(
        self,
        discord_user_id: int,
        username: str,
        user_german_level: str,
        user_mother_language: str,
        user_target_level: str,
        user_correction_style: str,
        user_input: str,
        user_message_history: list[dict]
    ) -> str | None:
        if not self.client:
            print("⚠️ Gemini client is not initialized.")
            return None

        try:
            formatted_history = self.format_history(user_message_history)
            prompt = self.build_prompt(
                discord_user_id=discord_user_id,
                username=username,
                user_german_level=user_german_level,
                user_mother_language=user_mother_language,
                user_target_level=user_target_level,
                user_correction_style=user_correction_style,
                user_input=user_input,
                formatted_history=formatted_history
            )

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )

            if response and hasattr(response, "text") and response.text:
                print("✅ Gemini Response:\n", response.text)
                return response.text

            print("⚠️ Empty response from Gemini")
            return None

        except Exception as error:
            print(f"⚠️ Error generating Gemini response: {error}")
            return None
