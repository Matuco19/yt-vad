from pytube import YouTube
from colorama import Fore, Style
s = Style.BRIGHT

#code by Matuco19
print(f"{s+Fore.BLUE} All rights reserved to Matuco19.")

def download_media(url, output_path='downloads', media_type='audio'):
    try:
      
        yt = YouTube(url)

        if media_type == 'audio':
            
            media_stream = yt.streams.filter(only_audio=True).first()
        elif media_type == 'video':
         
            media_stream = yt.streams.filter(only_video=True).first()
        else:
            print(f"{s+Fore.RED} not supported format, using audio type.")
            media_stream = yt.streams.filter(only_audio=True).first()
            return

        
        print(f"{s+Fore.RESET} Downloading {media_type}:{s+Fore.BLUE} {yt.title}")
        media_stream.download(output_path)
        print(f"{s+Fore.GREEN} Finished Download! {s+Fore.RESET}")

    except Exception as e:
        print(f"Shit! There is an error: {s+Fore.RED} {e} {s+Fore.RESET}")


url = input(f"{s+Fore.RESET} Put your URL: {s+Fore.BLUE} ")
download_media(url, media_type=input(f"{s+Fore.RESET} Video or audio(video/audio): "))