import ollama
from AIAgent_Config import OLLAMA_MODEL


class AIAgent_Ollama:
    def __init__(self):
        self.client = ollama.Client()


    def generate_response(self, text: str) -> str:
        response = self.client.chat(
            model=OLLAMA_MODEL,
            messages=[
                {
                    'role': 'user',
                    'content': f"""
                    - Write in an organized, clean manner, and skip lines if necessary.
                    - Describe what you know about this place in a friendly and charismatic way: {text}
                    """
                }
            ],
            options={
                "temperature": 0.7,
                "num_predict": 512,
                "top_p": 0.9,
            }
        )
        
        # Acesso via atributo de objeto
        return response.message.content