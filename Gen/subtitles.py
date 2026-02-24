import os
import time
import requests

BASE_URL = "https://api.assemblyai.com"

# =====================================
# OPTIONAL: Paste API here if you want
# If empty, console will ask for it
# =====================================
API_KEY = "" #enter your api key here 


def upload_file(filepath, api_key):
    headers = {"authorization": api_key}

    def file_reader(file, chunk_size=8 * 1024 * 1024):
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

    with open(filepath, "rb") as f:
        response = requests.post(
            f"{BASE_URL}/v2/upload",
            headers=headers,
            data=file_reader(f),
            timeout=600
        )

    response.raise_for_status()
    return response.json()["upload_url"]


def request_transcript(upload_url, api_key):
    headers = {"authorization": api_key}

    json_data = {
        "audio_url": upload_url,
        "speech_models": ["universal"]
    }

    response = requests.post(
        f"{BASE_URL}/v2/transcript",
        headers=headers,
        json=json_data,
        timeout=60
    )

    response.raise_for_status()
    return response.json()["id"]


def wait_for_completion(transcript_id, api_key):
    headers = {"authorization": api_key}
    endpoint = f"{BASE_URL}/v2/transcript/{transcript_id}"

    while True:
        response = requests.get(endpoint, headers=headers, timeout=60)
        result = response.json()

        if result["status"] == "completed":
            return

        if result["status"] == "error":
            raise RuntimeError(result["error"])

        print("Processing...")
        time.sleep(4)


def download_srt(transcript_id, api_key, output_path):
    headers = {"authorization": api_key}

    response = requests.get(
        f"{BASE_URL}/v2/transcript/{transcript_id}/srt",
        headers=headers,
        timeout=120
    )

    response.raise_for_status()

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(response.text)


def main():
    print("\n=== Simple Subtitle Generator ===\n")

    # If API_KEY is empty → ask user
    api_key = API_KEY.strip()
    if not api_key:
        api_key = input("Enter your AssemblyAI API Key: ").strip()

    video_path = input("Enter full video file path (.mp4): ").strip().strip('"')

    if not os.path.exists(video_path):
        print("❌ File not found.")
        return

    # Create Output folder in SAME directory as video
    video_folder = os.path.dirname(video_path)
    output_folder = os.path.join(video_folder, "Output")
    os.makedirs(output_folder, exist_ok=True)

    filename = os.path.splitext(os.path.basename(video_path))[0]
    output_path = os.path.join(output_folder, f"{filename}.srt")

    try:
        print("\nUploading file...")
        upload_url = upload_file(video_path, api_key)

        print("Requesting transcription...")
        transcript_id = request_transcript(upload_url, api_key)

        print("Waiting for completion...")
        wait_for_completion(transcript_id, api_key)

        print("Downloading subtitles...")
        download_srt(transcript_id, api_key, output_path)

        print(f"\n✅ Subtitle saved at:")
        print(output_path)

    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()