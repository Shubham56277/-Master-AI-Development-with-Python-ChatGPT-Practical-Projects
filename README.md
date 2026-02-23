# 🚀 Master AI Development with Python – Practical Projects

A collection of practical Python projects built for learning, experimentation, and real-world skill development.

> 💡 Some parts of this project were developed with the assistance of ChatGPT.

---

<details>
<summary>▶ 🎬 Video to Audio Converter (Click to Expand)</summary>

## 📌 Overview
A Python tool that converts video files (MP4, MKV, AVI, etc.) into compressed MP3 audio files.

---

## 🛠 Installation

```bash
pip install moviepy imageio-ffmpeg
```

---

## ⚙ How It Works

```text
1. Loads the video file
2. Extracts the audio track
3. Converts it to MP3
4. Saves output as compressed audio file
```

---

## ▶ How To Run

Set your file name inside script:

```python
video_file = "1.mp4"
output_file = "output.mp3"
```

Run:

```bash
python convert_video_to_audio.py
```

---

## 📂 Output
```
output.mp3
```

</details>

---

<details>
<summary>▶ 🔐 Password Manager (Click to Expand)</summary>

## 📌 Overview
A simple file-based Password Manager built using Python.

Features:
- Store account credentials
- Retrieve saved passwords
- Local file storage
- Lightweight and easy to use

---

## 🛠 Installation

No external libraries required.

---

## ⚙ How It Works

```text
1. User chooses to Add or Retrieve password
2. Credentials are saved inside passwords.txt
3. Data is stored locally
4. Retrieval searches file for matching account
```

---

## ▶ How To Run

```bash
python password_manager.py
```

---

## 📂 Storage File
```
passwords.txt
```

---

⚠ Do NOT upload real passwords to GitHub.

</details>

---

# 📁 Project Structure

```
CHATGPT COURSE/
│
├── Gen/
│   ├── convert_video_to_audio.py
│   ├── subtitles.py
│   ├── 1.mp4
│   ├── output.mp3
│   └── subtitles.srt
│
├── PasswordManager/
│   └── password_manager.py
│
├── passwords.txt
└── README.md
```

---

# 🎯 Skills Demonstrated

- Python File Handling
- Audio Processing
- CLI Tool Development
- Project Structuring
- Git & GitHub Usage

---

# 🤖 Built With Assistance From

ChatGPT – for logic refinement, debugging, and structuring guidance.

---

# 📜 License

MIT License