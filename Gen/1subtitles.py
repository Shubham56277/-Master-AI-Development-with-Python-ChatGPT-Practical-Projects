import os
import time
import requests

API_KEY = "" #paste your api key here
AUDIO_PATH = r"E:\768\videoplayback (1).mp4" #copy and paste file path
BASE_URL = "https://api.assemblyai.com"

headers = {"authorization": API_KEY}


def upload_file(path: str) -> str:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Audio/video file not found: {path}")

    with open(path, "rb") as f:
        res = requests.post(
            f"{BASE_URL}/v2/upload",
            headers=headers,
            data=f,
            timeout=120
        )

    if res.status_code >= 400:
        raise RuntimeError(f"Upload failed: {res.status_code} {res.text}")

    return res.json()["upload_url"]


def request_transcript(audio_url: str) -> str:
    payload = {
        "audio_url": audio_url,
        "speech_models": ["universal-2"]  # or ["universal-3-pro"]
    }

    res = requests.post(
        f"{BASE_URL}/v2/transcript",
        json=payload,
        headers=headers,
        timeout=60
    )

    if res.status_code >= 400:
        raise RuntimeError(f"Transcript request failed: {res.status_code} {res.text}")

    return res.json()["id"]


def wait_for_completion(transcript_id: str, poll_interval: int = 3) -> dict:
    endpoint = f"{BASE_URL}/v2/transcript/{transcript_id}"

    while True:
        res = requests.get(endpoint, headers=headers, timeout=30)
        if res.status_code >= 400:
            raise RuntimeError(f"Polling failed: {res.status_code} {res.text}")

        result = res.json()
        status = result.get("status")

        if status == "completed":
            return result
        if status == "error":
            raise RuntimeError(f"Transcription error: {result.get('error')}")

        print(f"[{time.strftime('%H:%M:%S')}] Status: {status} ... waiting")
        time.sleep(poll_interval)


def download_srt(transcript_id: str, out_file: str = "subtitles.srt") -> None:
    res = requests.get(
        f"{BASE_URL}/v2/transcript/{transcript_id}/srt",
        headers=headers,
        timeout=60
    )

    if res.status_code >= 400:
        raise RuntimeError(f"SRT download failed: {res.status_code} {res.text}")

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(res.text)


def main():
    if API_KEY == "YOUR_ASSEMBLYAI_API_KEY":
        raise ValueError("Please set your AssemblyAI API key in API_KEY.")

    print(f"[{time.strftime('%H:%M:%S')}] Uploading file...")
    audio_url = upload_file(AUDIO_PATH)

    print(f"[{time.strftime('%H:%M:%S')}] Requesting transcription...")
    transcript_id = request_transcript(audio_url)

    print(f"[{time.strftime('%H:%M:%S')}] Waiting for completion...")
    result = wait_for_completion(transcript_id)

    print("Transcript:")
    print(result.get("text", ""))

    print(f"[{time.strftime('%H:%M:%S')}] Downloading SRT...")
    download_srt(transcript_id, "subtitles.srt")
    print("Done. Saved as subtitles.srt")


if __name__ == "__main__":
    main()
