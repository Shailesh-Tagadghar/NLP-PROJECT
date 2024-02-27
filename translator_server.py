#pip install Flask SpeechRecognition googletrans==4.0.0-rc1

from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)

def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

@app.route('/')
def index():
    # return open('index.html').read()
    return open('index.html', encoding='utf-8').read()

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text_to_translate = data['text_to_translate']
    target_language = data['target_language']
    translated_text = translate_text(text_to_translate, target_language)
    return jsonify({'translated_text': translated_text})

if __name__ == "__main__":
    app.run(debug=True)
