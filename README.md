# call-analyzer
Call Analyzer est une application composée de plusieurs micro-services Docker qui permet d’analyser automatiquement une conversation téléphonique. Elle convertit d’abord l’audio en texte grâce au modèle Whisper, puis résume le contenu avec un modèle NLP, et enfin affiche les résultats via une interface web simple.
## 🚀 Fonctionnalités
- 🎤 Transcription audio → texte (Whisper)
- 🧠 Résumé automatique du texte
- 🐳 Architecture basée sur plusieurs micro-services Docker
- 🌐 Interface web simple (Streamlit ou Flask)
- 📦 API interne pour échanger entre services

---

## 🏗️ Architecture générale
L'application est composée de plusieurs conteneurs Docker :

- `audio-service` → reçoit un fichier audio
- `whisper-service` → transcrit l’audio
- `summary-service` → résume le texte
- `frontend` → interface web
- `api-gateway` → communication entre services

---

## ⚙️ Installation

### 1️⃣ Cloner le projet
```bash
git clone https://github.com/sondes-hamouda/call-analyzer.git
cd call-analyzer
