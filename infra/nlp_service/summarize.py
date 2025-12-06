# summarize.py
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# 🔹 Modèle de résumé OFFLINE (aucun download nécessaire)
# 🔹 Fonctionne sans Internet
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

@app.route('/')
def home():
    return jsonify({"message": "Service NLP opérationnel ✅"})

@app.route('/summarize', methods=['POST'])
def summarize_text():
    """
    Reçoit un texte (JSON) et renvoie un résumé.
    """
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({"error": "Aucun texte reçu"}), 400

        text = data['text']

        # 🔹 Générer le résumé
        summary = summarizer(text, max_length=80, min_length=20, do_sample=False)

        return jsonify({
            "status": "success",
            "summary": summary[0]['summary_text']
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

