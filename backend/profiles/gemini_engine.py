from google import genai
from decouple import config
import json


class GeminiEngine:
    def __init__(self):
        try:
            api_key = config("GEMINI_API_KEY")
            self.client = genai.Client(api_key=api_key)
            self.model = "gemini-2.5-flash"
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
        - Keep the conversation flowing in German.
        - Be playful, natural, and brief — not a teacher.
        - Correct mistakes based on their correction style using Discord markdown (**bold**, *italic*, `inline code`).
        - Never translate or explain unless asked.
        - If the user writes in another language, kindly nudge them back to German.
        - Do not start every response with greetings like "Hallo" or "Hey".
        - Do not ask questions unless the user explicitly asks you something.
        - Vary your sentence openings and avoid repetitive phrasing.

        🧠 User profile:
        - German Level: {user_german_level}
        - Target Level: {user_target_level}
        - Mother Language: {user_mother_language}
        - Correction Style: {user_correction_style}

        ⚡ Response rules:
        - Respond directly to the latest user message.
        - If correction is needed, apply it inline and continue naturally.
        - Keep tone light, witty, and conversational — like a friend hanging out.
        - Avoid filler, avoid unnecessary questions, avoid repeating greetings.
        - Use short sentences, emojis sparingly, and natural German slang if appropriate.
        - Use emojis ONLY IF NEEDED, otherwise dont highlight text or bolden it. just send normal text.
        - If you'll ever explain to the user. use the user mother language to explain anything and give an example.

        💬 Conversation so far:
        {formatted_history}

        🆕 Latest user message:
        User: {user_input}
        """
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
