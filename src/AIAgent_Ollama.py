import ollama
from AIAgent_Config import OLLAMA_MODEL


class AIAgent_Ollama:
    def __init__(self):
        self.client = ollama.Client()

    def generate_response(self, text: str) -> str:
        response = self.client.chat(
            model=OLLAMA_MODEL,
            # 'messages' PRECISA ser uma lista de dicionários com 'role' e 'content'
            messages=[
                {
                    'role': 'user',
                    'content': f'Write a brief, casual, and formatted description of the address: {text}'
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