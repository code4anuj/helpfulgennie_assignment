import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Speak Anything:")
            audio = self.recognizer.listen(source)
        return audio

    def recognize_speech(self, audio):
        try:
            text = self.recognizer.recognize_google(audio)
            print("You said: {}".format(text))
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

    def process(self):
        audio = self.listen()
        return self.recognize_speech(audio)
