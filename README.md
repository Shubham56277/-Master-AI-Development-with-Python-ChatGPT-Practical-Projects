# Master AI Development with Python – Practical Projects  

A collection of practical Python projects built for learning, experimentation, and real-world skill development.

Some parts of this project were developed with the assistance of ChatGPT.

---

<details>
<summary><strong>Video to Audio Converter (Click to Expand)</strong></summary>

## Overview

A Python-based tool that converts video files (MP4, MKV, AVI, etc.) into compressed MP3 audio files using **Pydub**.

---

## Features

- Extracts audio from video  
- Creates `Output` folder automatically  
- Saves MP3 with same filename  
- Lightweight and console-based  
- No hardcoded file names  

---

## Installation

Install required package:

```bash
pip install pydub
```

Make sure **FFmpeg** is installed and added to system PATH.

---

## How It Works

```text
1. User enters full video file path
2. Script extracts audio from video
3. Creates Output folder inside same directory
4. Saves MP3 using same filename
```

---

## How To Run

```bash
python vid2audio.py
```

Enter full video path when prompted:

```
E:\videos\videotemp.mp4
```

---

## Output

```
E:\videos\Output\videotemp.mp3
```

</details>

---

<details>
<summary><strong>Subtitle Generator (Click to Expand)</strong></summary>

## Overview

A simple console-based subtitle generator built using the AssemblyAI API.  
It uploads a video file, transcribes speech, and downloads subtitles in `.srt` format.

---

## Features

- Accepts full video file path  
- Smart API key handling (auto or prompt)  
- Chunked upload for stability  
- Creates `Output` folder automatically  
- Saves `.srt` with same filename  
- Clean console-based workflow  

---

## Installation

Install required package:

```bash
pip install requests
```

---

## How It Works

```text
1. User enters API key (if not hardcoded)
2. User enters video file path
3. Video is uploaded to AssemblyAI
4. Transcription is requested
5. Script waits until completed
6. Subtitle (.srt) file is downloaded
7. Saved inside Output folder
```

---

## How To Run

```bash
python subtitles.py
```

Example input:

```
E:\videos\videotemp.mp4
```

---

## Output

```
E:\videos\Output\videotemp.srt
```

</details>

---

<details>
<summary><strong>Password Manager (Click to Expand)</strong></summary>

## Overview

A simple file-based Password Manager built using Python.  
It stores and retrieves account credentials locally using text file storage.

---

## Features

- Add new account credentials  
- Retrieve saved passwords  
- Stores data in local file  
- Lightweight and dependency-free  
- CLI-based interface  

---

## Installation

No external libraries required.

---

## How It Works

```text
1. User selects an option (Add / Retrieve)
2. Credentials are stored inside passwords.txt
3. Data is saved locally
4. Retrieval searches for matching account name
```

---

## How To Run

```bash
python password_manager.py
```

---

## Storage File

```
passwords.txt
```

Important: Do not upload real passwords to GitHub.

</details>

---

## Project Structure

```text
CHATGPT COURSE/
│
├── Gen/
│   ├── subtitles.py
│   ├── vid2audio.py
│   └── Output/
│
├── PasswordManager/
│   └── password_manager.py
│
├── passwords.txt
└── README.md
```

---

## Skills Demonstrated

- Python file handling  
- API integration (AssemblyAI)  
- Audio processing with Pydub  
- CLI application development  
- Project organization  
- Error handling  
- Git and GitHub usage  

---

## Acknowledgment

This project was built as part of hands-on Python learning and was developed with structural and debugging assistance from ChatGPT.