# call-analyzer
Call Analyzer est une application composée de plusieurs micro-services Docker qui permet d’analyser automatiquement une conversation téléphonique. Elle convertit d’abord l’audio en texte grâce au modèle Whisper, puis résume le contenu avec un modèle NLP, et enfin affiche les résultats via une interface web simple.

### 🚀 Fonctionnalités

* 🎙️ **Transcription vocale** : convertit un fichier audio (mp3/wav) en texte.
* 🧠 **Résumé automatique** : extrait les idées principales de la conversation.
* 🌐 **Interface web** : téléversement du fichier audio + affichage du texte + résumé.
* 🗄️ **Base de données** : stockage des transcriptions et résumés (SQLite ou PostgreSQL).
* 🐳 **Architecture Docker complète** : chaque service tourne dans son propre conteneur.

### 🏗️ Architecture du projet

```
call-analyzer/
│
├── infra/
│   ├── whisper_service/    → service Speech-to-Text (Whisper)
│   ├── nlp_service/        → service de résumé (Transformers)
│   ├── web_interface/      → interface utilisateur
│   └── db/                 → base de données
│
└── docker-compose.yml
```

### 🎯 Objectif

Faciliter l’analyse rapide d’un appel téléphonique (SAV, support, réunions, etc.) en automatisant :

1. La conversion audio → texte
2. Le résumé automatique
3. L’enregistrement des résultats
