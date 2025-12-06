# app.py
from flask import Flask, request, jsonify
import whisper
import os

app = Flask(__name__)

# Charger le modèle Whisper (tu peux choisir "tiny", "base", "small", "medium", "large")
model = whisper.load_model("base")

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    # Vérifier qu’un fichier a bien été envoyé
    if 'audio' not in request.files:
        return jsonify({"error": "Aucun fichier audio reçu"}), 400
    
    audio_file = request.files['audio']
    path = os.path.join("/tmp", audio_file.filename)
    audio_file.save(path)

    # Exécuter la transcription
    result = model.transcribe(path)  # langue = français
    text = result["text"]

    return jsonify({"transcription": text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

