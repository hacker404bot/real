from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__, template_folder='templates')

# Braille dictionary mapping text to Unicode Braille patterns
braille_dict = {
    "a": "⠁", "b": "⠃", "c": "⠉", "d": "⠙", "e": "⠑", "f": "⠋", "g": "⠛", "h": "⠓", "i": "⠊", "j": "⠚",
    "k": "⠅", "l": "⠇", "m": "⠍", "n": "⠝", "o": "⠕", "p": "⠏", "q": "⠟", "r": "⠗", "s": "⠎", "t": "⠞",
    "u": "⠥", "v": "⠧", "w": "⠺", "x": "⠭", "y": "⠽", "z": "⠵", " ": " ", ".": "⠲", ",": "⠂", "?": "⠦",
    "1": "⠼⠁", "2": "⠼⠃", "3": "⠼⠉", "4": "⠼⠙", "5": "⠼⠑", 
    "6": "⠼⠋", "7": "⠼⠛", "8": "⠼⠓", "9": "⠼⠊", "0": "⠼⠚"
}

def text_to_braille(text):
    """Converts input text to Unicode Braille."""
    return ''.join(braille_dict.get(char.lower(), char) for char in text)

@app.route("/", methods=["GET", "POST"])
def index():
    braille_output = ""
    if request.method == "POST":
        input_text = request.form["text"]
        braille_output = text_to_braille(input_text)
    return render_template("index.html", braille_output=braille_output)


def convert_to_braille():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Please provide text in JSON body like {'text': 'hello'}"}), 400
    
    input_text = data["text"]
    braille = text_to_braille(input_text)
    return jsonify({
        "text": input_text,
        "braille": braille
    })

if __name__ == "__main__":
    # Local dev only — Render uses gunicorn
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
