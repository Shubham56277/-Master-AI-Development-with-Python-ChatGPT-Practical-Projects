from pydub import AudioSegment
import os

# =====================================
# OPTIONAL: Default bitrate
# =====================================
DEFAULT_BITRATE = "64k"


def convert_video_to_audio(video_path, bitrate=DEFAULT_BITRATE):
    try:
        if not os.path.exists(video_path):
            print("❌ Video file not found!")
            return

        # Get video folder
        video_folder = os.path.dirname(video_path)

        # Create Output folder in same directory
        output_folder = os.path.join(video_folder, "Output")
        os.makedirs(output_folder, exist_ok=True)

        # Same filename, different extension
        filename = os.path.splitext(os.path.basename(video_path))[0]
        output_path = os.path.join(output_folder, f"{filename}.mp3")

        print("\nConverting...")

        # Load video and extract audio
        audio = AudioSegment.from_file(video_path)

        # Export as MP3
        audio.export(output_path, format="mp3", bitrate=bitrate)

        print("✅ Conversion Successful!")
        print("Saved at:")
        print(output_path)

    except Exception as e:
        print("❌ Error:", e)


if __name__ == "__main__":
    print("\n=== Video to Audio Converter ===\n")

    video_file = input("Enter full video file path (.mp4): ").strip().strip('"')

    convert_video_to_audio(video_file)