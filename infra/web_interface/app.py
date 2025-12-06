import streamlit as st
import requests

st.set_page_config(
    page_title="🎙️ Analyse intelligente d'appel",
    page_icon="🎧",
    layout="wide"
)

st.title("🎙️ Analyse intelligente d'appel")
st.markdown("Bienvenue dans votre outil d'analyse audio intelligent ! 🎤")

# --- Section d'upload et choix ---
with st.sidebar:
    st.header("Paramètres")
    summary_type = st.selectbox("Type de résumé :", ["Court", "Long"])
    st.markdown("💡 Téléversez un fichier audio et choisissez le type de résumé.")

audio_file = st.file_uploader("📂 Sélectionnez un fichier audio", type=["wav", "mp3"])

# --- Initialisation du session_state ---
if "transcription" not in st.session_state:
    st.session_state.transcription = ""
if "summary" not in st.session_state:
    st.session_state.summary = ""
if "last_summary_type" not in st.session_state:
    st.session_state.last_summary_type = summary_type

# --- Fonction pour générer le résumé ---
def generate_summary(text, summary_type):
    try:
        with st.spinner("⏳ Résumé en cours..."):
            res = requests.post(
                "http://nlp_service:5002/summarize",
                json={"text": text, "summary_type": summary_type}
            )
        if res.status_code == 200:
            st.session_state.summary = res.json().get("summary", "")
            st.session_state.last_summary_type = summary_type
            st.success("💡 Résumé généré !")
        else:
            st.error("❌ Erreur lors de la génération du résumé (service NLP).")
    except Exception as e:
        st.error(f"⚠️ Une erreur est survenue lors du résumé : {e}")

# --- Bouton pour analyser / recalculer le résumé ---
if audio_file:
    if st.button("▶️ Analyser l'appel") or (st.session_state.transcription and summary_type != st.session_state.last_summary_type):
        # Si transcription déjà faite et juste changement de type de résumé
        if st.session_state.transcription:
            generate_summary(st.session_state.transcription, summary_type)
        else:
            # Sinon, lancer la transcription
            try:
                st.info("📤 Envoi du fichier au service de transcription...")
                files = {"audio": (audio_file.name, audio_file, audio_file.type)}

                with st.spinner("⏳ Transcription en cours..."):
                    response = requests.post("http://whisper_service:5001/transcribe", files=files)

                if response.status_code == 200:
                    text = response.json().get("transcription", "")
                    st.session_state.transcription = text
                    st.success("✅ Transcription terminée !")
                    
                    st.subheader("🗒️ Transcription")
                    st.text_area("Texte complet", value=text, height=200, key="transcription_area")

                    # Générer le résumé
                    generate_summary(text, summary_type)
                else:
                    st.error("❌ Erreur lors de la transcription (service Whisper).")
            except Exception as e:
                st.error(f"⚠️ Une erreur est survenue : {e}")

# --- Affichage de la transcription et résumé existants ---
if st.session_state.transcription:
    st.subheader("🗒️ Transcription")
    st.text_area("Texte complet", value=st.session_state.transcription, height=200, key="transcription_area2")

if st.session_state.summary:
    st.subheader("✨ Idées principales")
    st.text_area("Résumé", value=st.session_state.summary, height=150, key="summary_area2")

# --- Section d'historique ---
st.markdown("---")
st.subheader("📜 Historique")
st.info("Les dernières analyses apparaîtront ici (à implémenter si nécessaire).")

