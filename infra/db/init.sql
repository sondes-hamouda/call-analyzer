-- Création de la base (si nécessaire)
CREATE TABLE IF NOT EXISTS calls (
    id SERIAL PRIMARY KEY,
    audio_filename VARCHAR(255),
    transcription TEXT,
    summary TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

