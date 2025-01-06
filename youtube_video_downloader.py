import yt_dlp
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()

def download_playlist(url, download_path='.'):
    ydl_opts = {
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',
        'format': 'best', 
        'noplaylist': False, 
        'progress_hooks': [my_hook],
        'ignoreerrors': True, 
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        print(f"Error: {e}")

def my_hook(d):
    if d['status'] == 'downloading':
        print(f"Downloading {d['filename']} - {d['_percent_str']} {d['_speed_str']}")
    elif d['status'] == 'finished':
        print(f"Finished downloading {d['filename']}")

def handle_private_video_error(video_url):
    logger.warning(f"Video '{video_url}' is private or unavailable. Skipping it.")

if __name__ == "__main__":
    playlist_url = 'https://www.youtube.com/playlist?list=PL9gnSGHSqcnoqBXdMwUTRod4Gi3eac2Ak'

    download_path = '.' 
    download_playlist(playlist_url, download_path)
