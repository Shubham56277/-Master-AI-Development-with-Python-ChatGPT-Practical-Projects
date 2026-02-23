from pydub import AudioSegment
import os

def convert_video_to_audio(video_path, output_path, bitrate="64k"):
    try:
        if not os.path.exists(video_path):
            print("❌ Video file not found!")
            return
        
        # Load video file (pydub automatically extracts audio)
        audio = AudioSegment.from_file(video_path)
        
        # Export as MP3
        audio.export(output_path, format="mp3", bitrate=bitrate)
        
        print("✅ Conversion Successful!")

    except Exception as e:
        print("❌ Error:", e)


if __name__ == "__main__":
    video_file = "1.mp4"
    output_file = "output.mp3"

    convert_video_to_audio(video_file, output_file)