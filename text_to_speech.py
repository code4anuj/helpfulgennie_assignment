from gtts import gTTS

class TextToSpeech:
    def __init__(self, text, language='en', slow=False, filename='output.mp3'):
        self.text = text
        self.language = language
        self.slow = slow
        self.filename = filename

    def convert_to_speech(self):
        # Convert text to speech
        tts = gTTS(text=self.text, lang=self.language, slow=self.slow)
        tts.save(self.filename)
        print(f"Saved audio to {self.filename}")

    def process(self):
        # Complete process: convert text to speech
        self.convert_to_speech()
