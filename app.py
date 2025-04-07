import speech_recognition as sr
from flask import Flask

app = Flask(__name__)


# Braille dictionary mapping text to Unicode Braille patterns
braille_dict = {
    "a": "⠁", "b": "⠃", "c": "⠉", "d": "⠙", "e": "⠑", "f": "⠋", "g": "⠛", "h": "⠓", "i": "⠊", "j": "⠚",
    "k": "⠅", "l": "⠇", "m": "⠍", "n": "⠝", "o": "⠕", "p": "⠏", "q": "⠟", "r": "⠗", "s": "⠎", "t": "⠞",
    "u": "⠥", "v": "⠧", "w": "⠺", "x": "⠭", "y": "⠽", "z": "⠵", " ": " ", ".": "⠲", ",": "⠂", "?": "⠦","1": "⠼⠁", "2": "⠼⠃", "3": "⠼⠉", "4": "⠼⠙", "5": "⠼⠑", 
    "6": "⠼⠋", "7": "⠼⠛", "8": "⠼⠓",
    "9": "⠼⠊", "0": "⠼⠚"

}

def text_to_braille(text):
    """Converts text to Braille using Unicode Braille patterns."""
    return ''.join(braille_dict.get(char.lower(), char) for char in text)

def audio_to_braille():
    """Captures audio, converts it to text, and then to Braille."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print(f"Recognized Text: {text}")
            braille_text = text_to_braille(text)
            print(f"Braille Output: {braille_text}")
            return braille_text
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError:
            print("Speech recognition service unavailable.")

if __name__ == "__main__":
    audio_to_braille()
