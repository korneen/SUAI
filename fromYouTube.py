from pytube import YouTube

video_url = "https://www.youtube.com/watch?v=hgI0p1zf31k"

yt = YouTube(video_url)

stream = yt.streams.get_highest_resolution()

output_path = "path/to/output/directory/"

stream.download(output_path