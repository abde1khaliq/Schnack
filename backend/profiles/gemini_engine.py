from google import genai
from decouple import config


class GeminiEngine:
    def __init__(self):
        try:
            api_key = config("GEMINI_API_KEY")
            self.client = genai.Client(api_key=api_key)
            self.model = "gemini-2.5-flash"
        except Exception as error:
            print(f"⚠️ Error initializing Gemini client: {error}")
            self.client = None

    def generate_prompt_based_on_user_preferences(
        self,
        discord_user_id: int,
        username: str,
        user_german_level: str,
        user_mother_language: str,
        user_target_level: str,
        user_correction_style: str,
        user_input: str,
    ) -> str:
        return f"""
    You are a casual German-speaking friend chatting with {username}. 
    Do not act like a teacher — keep responses short, natural, and playful.

    User context:
    - Current German Level: {user_german_level}
    - Target Level: {user_target_level}
    - Mother Language: {user_mother_language}
    - Correction Style: {user_correction_style}

    The user's latest German message:
    > {user_input}

    Guidelines:
    - Respond ONLY in German. If the user writes in another language, remind them kindly to switch back to German.
    - Keep replies short and conversational — no long explanations.
    - Do not translate or explain anything unless the user explicitly asks for the meaning of a word or phrase.
    - If they make a mistake (grammar, verbs, articles), correct it briefly and clearly using Discord markdown (**bold**, *italic*, `inline code`).
    - Avoid unnecessary spacing or formatting. Keep it tight and natural.
    - Your goal: keep the conversation flowing in German, make it fun, and nudge them to improve by responding directly to what they say.
    """

    def get_response(
        self,
        discord_user_id: int,
        username: str,
        user_german_level: str,
        user_mother_language: str,
        user_target_level: str,
        user_correction_style: str,
        user_input: str,
    ) -> str | None:
        if not self.client:
            print("⚠️ Gemini client is not initialized.")
            return None

        try:
            prompt = self.generate_prompt_based_on_user_preferences(
                discord_user_id=discord_user_id,
                username=username,
                user_german_level=user_german_level,
                user_mother_language=user_mother_language,
                user_target_level=user_target_level,
                user_correction_style=user_correction_style,
                user_input=user_input,
            )

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )

            if response and hasattr(response, "text") and response.text:
                return response.text  # Raw output for testing

            print("⚠️ Empty response from Gemini")
            return None

        except Exception as error:
            print(f"⚠️ Error generating Gemini response: {error}")
            return None
