from google import genai
from config import GENAI_API_KEY
from AIAgent_Config import GENAI_MODEL


class AIAgent_Gemini:
    def __init__(self):
        # Usar api_key é a forma padrão documentada no SDK
        self.client = genai.Client(api_key=GENAI_API_KEY)

    def generate_response(self, text: str) -> str:
        response = self.client.models.generate_content(
            model=GENAI_MODEL,
            contents=f'Write a brief, casual description of the address: {text}'
        )
        return response.text