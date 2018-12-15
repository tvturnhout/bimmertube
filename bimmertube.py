# -*- coding: utf-8 -*-
import os
import shutil
import sys

def main():
    if len(sys.argv > 1):
        url = sys.argv[1]
    else:
        raise Exception('YouTube-playlist URL required.')

    # Create folders
    shutil.rmtree('temp', ignore_errors=True)
    os.mkdir('temp')
    shutil.rmtree('output', ignore_errors=True)
    os.mkdir('output')
    os.chdir('temp')

    # Download the entire playlist
    command = 'youtube-dl -i \
               --no-check-certificate \
               --merge-output-format mp4 \
               --format bestvideo[ext=mp4]+bestaudio[ext=m4a] \
               "' + url + '"'

    os.system(command)

    # Convert files to the format suitable for the BMW 4-series
    for fn in os.listdir():
        command = 'ffmpeg -i "'+ fn +'" \
                   -vf "scale=1280:ih*1280/iw, crop=1280:480" \
                   "../output/' + fn + '"'

        os.system(command)

    # Clean-up
    shutil.rmtree('temp', ignore_errors=True)


if __name__ == '__main__':
    main()