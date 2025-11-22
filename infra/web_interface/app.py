# app.py
import streamlit as st
import requests

st.title("🎙️ Analyse intelligente d’appel")

# 1️⃣ Téléversement d’un fichier audio
audio_file = st.file_uploader("Téléverse un fichier audio", type=["wav", "mp3"])

if audio_file:
    st.info("Envoi du fichier au service de transcription...")

    # 2️⃣ Envoi du fichier au service Whisper
    files = {"audio": audio_file.getvalue()}
    response = requests.post("http://whisper_service:5001/transcribe", files={"audio": audio_file})

    if response.status_code == 200:
        text = response.json()["transcription"]
        st.subheader("🗒️ Transcription")
        st.write(text)

        st.info("Résumé en cours...")
        # 3️⃣ Envoi du texte au service NLP
        res = requests.post("http://nlp_service:5002/summarize", json={"text": text})

        if res.status_code == 200:
            st.subheader("💡 Idées principales")
            st.write(res.json()["summary"])
        else:
            st.error("Erreur dans le service NLP")
    else:
        st.error("Erreur dans la transcription")

