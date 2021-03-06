#!/usr/bin/env python3


import os, youtube_dl, re, sys, shutil


def remove_webm_files():
    """
	.webm files are useless after the 
	conversion to mp3 was done.
	So, this function removes
	all these files from the folder.
	"""
    for file in os.listdir('.'):
	    if re.search('.*webm', file):
		    print('Removed :', file)
		    os.remove(file)


def move_mp3_files():
    """
    mp3 files will be moved in the 
    Downloaded folder.
    """
    for file in os.listdir('.'):
         if re.search(".*mp3", file):
              print('Moving', file, ' ...')
              shutil.copy(file, 'Downloaded/' + file)
              os.remove(file)

			
def download_song(link_to_song):
    """
	download and convert to mp3
	from YouTube.
	This entire code was copy/pasted
	from the internet. :(
	At least I understood it :)
	"""
    download_options = {
    'format': 'bestaudio/best',
	'outtmpl': '%(title)s.%(ext)s',
	'nocheckcertificate': True, 
# this one ^ can be removed if there are errors because of it
 	'postprocessors': [{
	    'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
		}]
		}

    with youtube_dl.YoutubeDL(download_options) as dl:
        dl.download([link_to_song])
	

if len(sys.argv) < 2:
    print('Please provide a link to a song!')
elif len(sys.argv) > 2:
    print("Only one song at a time, please!")
else:
    link_to_song = sys.argv[1]
    download_song(link_to_song)
    remove_webm_files()
    move_mp3_files()

