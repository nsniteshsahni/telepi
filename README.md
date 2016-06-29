# telepy
A simple,intuitive telegram bot made for interaction and data fetching from Raspberry pi.Currently this ChatBot is hotsted on Microsoft Azure for prompt and lag free responses.You can access the demo @https://telegram.me/nsniteshsahni_bot 

# Examples
To interact with bot,you can reference the following examples

```
/hi
```
To greet your device


```
/wiki Delhi
```
It will perform a wikipedia search and returns the relevant data without any clutter
```
/torrent <magnet link/torrent URL/info hash>
```
Adds and downloads torrent remotely to your device.Uses deluge torrent client as backend.
Visit above bot URL for more interesting features and commands.
# Requirements  
This bot requires following Python librarires:
- Wikipedia
- OpenWeatherMap
- Python wrapper class for telegram
- Deluge torrent client
- Speedtest cli
- Beautiful Soup

# Installation
```
sudo pip install wikipedia
sudo pip install pyowm
sudo pip install telepot
sudo pip install pyshorteners
sudo pip install speedtest-cli
sudo pip install bs4
sudo pip install requests
sudo apt-get install deluge
```
Install deluge torrent client for remote torrent downloading feature.
Now just simply run bot.py and attach it to startup process for uninterrupted operation

#List of features
1. Weather Status
2. Torrent Downloading
3. Wikipedia Search
4. Network  Speedtest
5. Google News Headlines

And other auxiliary features

# API Reference
1. Wikipedia for data fetching
2. OpenWeatherMaps for weather details
3. GPIO Library for python
4. Telegram API for bot
5. Google API for URL Shortening
6. Beautiful soup for web parsing
7. Deluge Console API for remote torrent downloading

# License
The MIT License (MIT)

Copyright (c) 2016 Nitesh Sahni

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
