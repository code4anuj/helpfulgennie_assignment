import ollama

class AiChat:
    def __init__(self):
        pass

    def generate_response(self, question):
        print("Thinking...")
        response = ollama.chat(model='llama3', messages=[
            {
                'role': 'user',
                'content': question,
            },
        ])
        print("Generation Done")
        return response['message']['content']