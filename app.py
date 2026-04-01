import streamlit as st
from audio_recorder_streamlit import audio_recorder
import pandas as pd
import os
import time

# -------------------------
# CONFIG
# -------------------------
st.set_page_config(page_title="Speech Collector", layout="centered")

st.title("🎙️ VoiceLab — Speech Dataset Collector")
st.caption("Record speech easily (Browser-based 🎙️)")

# -------------------------
# INIT
# -------------------------
if not os.path.exists("recordings"):
    os.makedirs("recordings")

# -------------------------
# USER INFO
# -------------------------
st.subheader("👤 User Information")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=5, max_value=100)

with col2:
    gender = st.selectbox("Gender", ["Select", "Male", "Female", "Other"])
    language = st.selectbox("Language", [
        "English", "Hindi", "Marathi", "Gujarati",
        "Tamil", "Telugu", "Kannada", "Bengali"
    ])

# -------------------------
# AUDIO RECORDER
# -------------------------
st.subheader("🎙️ Record Audio")
st.info("Click 🎙️ to start recording, click again to stop")

# ✅ audio_recorder returns WAV bytes directly — no pyaudio needed
audio_bytes = audio_recorder(
    text="Click to record",
    recording_color="#e74c3c",
    neutral_color="#2ecc71",
    icon_size="2x"
)

if audio_bytes:
    st.success("✅ Recording complete!")

    # Playback
    st.audio(audio_bytes, format="audio/wav")

    # -------------------------
    # TEXT INPUT
    # -------------------------
    text = st.text_area("📝 What did you say?")

    if st.button("💾 Save Data"):
        if not name or gender == "Select" or not text:
            st.warning("⚠️ Please fill all fields before saving.")
        else:
            # Save audio file only after validation
            filename = f"{name}_{int(time.time())}.wav"
            filepath = os.path.join("recordings", filename)

            with open(filepath, "wb") as f:
                f.write(audio_bytes)

            data = {
                "name": name,
                "age": age,
                "gender": gender,
                "language": language,
                "text": text,
                "audio_path": filepath
            }

            df = pd.DataFrame([data])

            file_exists = os.path.exists("dataset.csv")
            df.to_csv(
                "dataset.csv",
                mode='a',
                header=not file_exists,
                index=False,
                quoting=1
            )

            st.success("🎉 Data saved successfully!")
            st.balloons()

# -------------------------
# DATA PREVIEW
# -------------------------
st.subheader("📊 Dataset Preview")

if os.path.exists("dataset.csv"):
    df = pd.read_csv("dataset.csv", on_bad_lines='skip')
    st.write(f"Total Records: **{len(df)}**")
    st.dataframe(df.tail(10))
else:
    st.info("No data recorded yet. Start recording to build your dataset!")

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.title("📘 Instructions")
st.sidebar.write("""
1. Fill user info  
2. Click 🎙️ to record  
3. Click again to stop  
4. Enter what you said  
5. Click 💾 Save  
""")

st.sidebar.success("🚀 Stable Recording Enabled!")

st.sidebar.markdown("---")
st.sidebar.title("📁 Dataset Info")
if os.path.exists("dataset.csv"):
    df_info = pd.read_csv("dataset.csv", on_bad_lines='skip')
    st.sidebar.metric("Total Recordings", len(df_info))
else:
    st.sidebar.info("No dataset yet.")
