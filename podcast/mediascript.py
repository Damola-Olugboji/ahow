from __future__ import unicode_literals
import os, sys, time, datetime
from selenium import webdriver
from pydub import AudioSegment
import youtube_dl
import glob

podcast_dir = r"C:\Users\Damola\Desktop\code\ahow\podcast"
path_to_intro = r"C:\Users\Damola\Desktop\code\ahow\podcast\fixed\podcast_intro.mp3"
# driver = webdriver.Chrome(
#    executable_path=r"C:\Users\Damola\Desktop\chromedriver_win32\chromedriver.exe"
# )
# driver.get("http://seleniumhq.org/")


def file_scraping(website, start_time, end_time):
    start_time = start_time * 1000
    end_time = end_time * 1000
    extension_list = ["*.mp3"]

    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([website])
        print("Download Complete")
    intro_audio = AudioSegment.from_mp3(path_to_intro)

    sermon_songs = [AudioSegment.from_mp3(mp3_file) for mp3_file in glob.glob("*.mp3")]
    sermon_audio = sermon_songs.pop(0)
    sermon_audio = sermon_audio[start_time:end_time]

    final_file = intro_audio + sermon_audio
    final_file.export(
        r"C:\Users\Damola\Desktop\code\ahow\podcast\fixed\final.mp3", format="mp3"
    )


file_scraping(
    website="https://www.youtube.com/watch?v=M-mtdN6R3bQ", start_time=10, end_time=20
)
