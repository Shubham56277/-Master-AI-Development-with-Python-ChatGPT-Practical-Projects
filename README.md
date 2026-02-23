<details>
<summary><b>▶ Subtitle Gen (Click to Expand)</b></summary>

---

### 1️⃣ Installation

Install required package:

```bash
pip install requests
```

---

### 2️⃣ API Key Setup

Create account at:  
https://www.assemblyai.com  

Generate your API key and paste inside script:

```python
API_KEY = "YOUR_ASSEMBLYAI_API_KEY"
```

⚠ Do NOT upload your API key to GitHub.

---

### 3️⃣ How It Works

```text
Step 1 → Upload local file
Step 2 → Request transcription
Step 3 → Poll until status = completed
Step 4 → Download subtitles as .srt
```

---

### 4️⃣ How To Run

Set your file path:

```python
AUDIO_PATH = r"E:\path\to\video.mp4"
```

Run:

```bash
python subtitles.py
```

Output:

```text
subtitles.srt
```

</details>
