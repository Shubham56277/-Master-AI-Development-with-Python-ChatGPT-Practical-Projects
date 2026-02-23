# Master AI Development with Python – Practical Projects

A collection of practical Python projects built for learning, experimentation, and real-world skill development.

Some parts of this project were developed with the assistance of ChatGPT.

---

## About This Repository

This repository contains beginner-to-intermediate level Python projects focused on:

- Practical implementation
- Clean code structure
- Real-world use cases
- Command-line tools
- File handling and media processing

---

<details>
<summary><strong>Video to Audio Converter (Click to Expand)</strong></summary>

## Overview

A Python-based tool that converts video files (MP4, MKV, AVI, etc.) into compressed MP3 audio files using MoviePy.

---

## Features

- Extracts audio from video  
- Supports multiple video formats  
- Adjustable bitrate  
- Simple and lightweight  
- Command-line based execution  

---

## Installation

Install required packages:

```bash
pip install moviepy imageio-ffmpeg
```

---

## How It Works

```text
1. Loads the video file
2. Extracts the audio stream
3. Converts it into MP3 format
4. Saves the output file locally
```

---

## How To Run

Edit inside the script if needed:

```python
video_file = "1.mp4"
output_file = "output.mp3"
```

Run the script:

```bash
python convert_video_to_audio.py
```

---

## Output

```
output.mp3
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

## Skills Demonstrated

- Python file handling  
- Media processing with MoviePy  
- Command-line interface development  
- Project organization  
- Dependency management  
- Git and GitHub usage  

---

## Future Improvements

- GUI version using Tkinter  
- Encryption for password storage  
- Batch video conversion  
- Logging system  
- Packaging as executable (.exe)  

---

## License

This project is licensed under the MIT License.

---

## Acknowledgment

This project was built as part of hands-on Python learning and was developed with structural and debugging assistance from ChatGPT.