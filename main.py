from pytube import YouTube
import sys

url = input("Enter a URL: ")
yt = YouTube(url)

print('Title:', yt.title)
print('Views:', yt.views)

 
yd = yt.streams.get_highest_resolution()

yd.download("D:/PYTHON/1PRACE/downloaderyt")