# BMW 4-series Pro navigation YouTube-downloader
This downloader can be used to download any YouTube-playlist to a format that fits on the BMW 4-series Pro navigation screen.

## Requirements
- Python 3.7
- ffmpeg (either in same directory or configured in `PATH`-variable)

## How-to
### Installation
Clone this repository:
```bash
git clone https://github.com/koenvaneijk/bimmertube
cd bimmertube
pip install -r requirements.txt
```
### Usage
```bash
python bimmertube.py https://www.youtube.com/playlist?list=PLwl7RmKyO23wRhaT6AXvur6E-mIDuqRjt
```
The script will start with downloading all videos in your playlist to a temporary directory (`temp`). It then proceeds with converting the videos to the format that is suitable for your BMW 4-series. Resulting videos will end up in the `output` directory.

## Remarks
Script is tested on Windows 10 Pro with Python 3.7.

## Credits
This script is a wrapper around [ffmpeg](https://www.ffmpeg.org/) and [youtube-dl](http://rg3.github.io/youtube-dl/). All credits goes to them.
