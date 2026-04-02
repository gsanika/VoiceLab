# 🎙️ VoiceLab — Speech Dataset Collector

A production-ready Streamlit app for collecting high-quality, labeled speech recordings across multiple languages. Built for researchers, ML engineers, and linguists building ASR/TTS datasets.

---

## Features

| Feature | Description |
|---------|-------------|
| **20 Languages** | English, Hindi, Marathi, Tamil, Telugu, Kannada, Bengali, Gujarati, Punjabi, Malayalam, Odia, Assamese, French, German, Spanish, Japanese, Mandarin, Arabic, Portuguese, Russian |
| **Rich Metadata** | Name, gender, age, language, recording |
| **Live Stats Sidebar** | Real-time count of recordings, languages, and per-language breakdown |
| **Configurable Audio** | Duration (2–30s), sample rate (22 / 44.1 / 48 kHz) |
| **Dataset Filters** | Filter preview by language, gender, or speaker name |
| **CSV Export** | Download full or filtered dataset with one click |
| **Smart Filenames** | `SpeakerName_Language_YYYYMMDD_HHMMSS.wav` |

---

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```


### 2. Run the app

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## File Structure

```
project/
├── app.py   ← Main app
├── README.md             ← This file
├── dataset.csv           ← Auto-created on first save
└── recordings/           ← Auto-created; WAV files stored here
    ├── Priya_Hindi_20241201_143022.wav
    ├── Alex_English_20241201_143512.wav
    └── ...
```

---

## Dataset CSV Schema

| Column | Type | Description |
|--------|------|-------------|
| `name` | string | Speaker's name |
| `gender` | string | Female / Male / Non-binary / Prefer not to say |
| `age` | string | Under 18 / 18–25 / 26–35 / 36–45 / 46–60 / 60+ |
| `language` | string | Speaking language |
| `text` | string | Spoken sentence(s) |
| `audio_path` | string | Relative path to WAV file |

---

## Workflow

```
1. Fill Speaker Info
   └─ Name, Gender, Age, Language, text,audio_path

2. Choose Speech Text
   ├─ Write your own sentence
   └─ Pick from categorised sample prompts (Everyday / Numbers / Questions / Technical)

3. Record
   ├─Click Start Recording by clicking on mice
   ├─ Record your voice
   └─ Stop recording using Stop Recording button

4. Review & Save
   ├─ Playback the recording
   ├─ Review all metadata
   └─ Save → appended to dataset.csv
```

---

## Tips for High-Quality Data

- Use a quiet room with minimal echo
- Hold the mic 15–20 cm from your mouth
- Record multiple speakers for a diverse dataset
- Use the "Excellent" quality rating only for clean, artifact-free audio
- Record the same sentence in different languages for parallel corpora

---

## Requirements

```
streamlit
audio-recorder-streamlit
pandas
```
