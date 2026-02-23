# -Master-AI-Development-with-Python-ChatGPT-Practical-Projects
<details> <summary><b>1. Installation (Click to Expand)</b></summary>

Install required package:

pip install requests
</details>
<details> <summary><b>2. API Key Setup (Click to Expand)</b></summary>

Create an account at:
https://www.assemblyai.com

Generate your API key and paste it inside the script:

API_KEY = "YOUR_ASSEMBLYAI_API_KEY"

⚠ Do NOT upload your API key to GitHub.

</details>
<details> <summary><b>3. How It Works (Click to Expand)</b></summary>

Step 1 → Upload local file to AssemblyAI
Step 2 → Request transcription
Step 3 → Poll until status becomes "completed"
Step 4 → Download subtitles as .srt

</details>
<details> <summary><b>4. How To Run (Click to Expand)</b></summary>

Make sure your file path is correct:

AUDIO_PATH = r"E:\path\to\your\video.mp4"

Run the script:

python subtitles.py

After completion, you will get:

subtitles.srt
</details>