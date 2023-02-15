from pytube import YouTube

# create a YouTube object for the video you want to download
yt = YouTube("https://www.youtube.com/watch?v=UT5F9AXjwhg")

# Select the highest quality stream
stream = yt.streams.get_highest_resolution()

# Download the video to your current working directory
stream.download()
