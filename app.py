import streamlit as st
from audiorecorder import audiorecorder
import pandas as pd
import os
import time

# -------------------------
# CONFIG
# -------------------------
st.set_page_config(page_title="Speech Collector", layout="centered")

st.title("🎤 Speech Data Collection App")
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
# 🎤 AUDIO RECORDER (BEST PART)
# -------------------------
st.subheader("🎙️ Record Audio")

st.info("Click mic ▶️ speak ▶️ click again to stop")

audio = audiorecorder("▶️ Start Recording", "⏹️ Stop Recording")

if len(audio) > 0:
    st.success("✅ Recording complete!")

    # Playback
    st.audio(audio.export().read())

    # Save file
    filename = f"{name}_{int(time.time())}.wav"
    filepath = os.path.join("recordings", filename)

    with open(filepath, "wb") as f:
        f.write(audio.export().read())

    # -------------------------
    # TEXT INPUT
    # -------------------------
    text = st.text_area("📝 What did you say?")

    if st.button("💾 Save Data"):
        if not name or gender == "Select" or not text:
            st.warning("⚠️ Fill all fields")
        else:
            data = {
                "name": name,
                "age": age,
                "gender": gender,
                "language": language,
                "text": text,
                "audio_path": filepath
            }

            df = pd.DataFrame([data])

            df.to_csv(
                "dataset.csv",
                mode='a',
                header=not os.path.exists("dataset.csv"),
                index=False,
                quoting=1
            )

            st.success("🎉 Data saved!")

# -------------------------
# DATA PREVIEW
# -------------------------
st.subheader("📊 Dataset Preview")

if os.path.exists("dataset.csv"):
    df = pd.read_csv("dataset.csv", on_bad_lines='skip')
    st.dataframe(df.tail(10))
else:
    st.info("No data yet")

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.title("📘 Instructions")
st.sidebar.write("""
1. Fill user info  
2. Click ▶️ to record  
3. Click ⏹️ to stop  
4. Enter text  
5. Save  
""")

st.sidebar.success("🚀 Stable Recording Enabled!")