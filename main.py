from pytube import YouTube
#code by Matuco19
print("All rights reserved to Matuco19.")

def download_media(url, output_path='downloads', media_type='audio'):
    try:
      
        yt = YouTube(url)

        if media_type == 'audio':
            
            media_stream = yt.streams.filter(only_audio=True).first()
        elif media_type == 'video':
         
            media_stream = yt.streams.filter(only_video=True).first()
        else:
            print("not supported format, using audio type.")
            media_stream = yt.streams.filter(only_audio=True).first()
            return

        
        print(f"Downloading {media_type}: {yt.title}")
        media_stream.download(output_path)
        print("Finished Download! Content moved to 'downloads' folder.")

    except Exception as e:
        print(f"Shit! There is an error: {e}")


url = input("Put your URL: ")
download_media(url, media_type=input("Video or audio(video/audio): "))
