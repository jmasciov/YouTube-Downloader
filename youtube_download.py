from pytube import YouTube

# URL of video to install
video_url = "https://www.youtube.com/watch?v=Xacn34M_vHA"
yt = YouTube(video_url)

# best audio

stream = yt.streams.filter(only_audio=True)

# best video resolution
# stream = yt.streams.get_highest_resolution()

stream[0].download()


print(f'Download complete: {yt.title}')