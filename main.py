import yt_dlp
import argparse
import os


def download_audio(url, output_dir="downloads"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "outtmpl": f"{output_dir}/%(title)s.%(ext)s",
        "quiet": False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Audio Downloader")
    parser.add_argument("url", help="URL to download")
    parser.add_argument("--dir", help="Output directory", default="downloads")
    args = parser.parse_args()

    download_audio(args.url, args.dir)
