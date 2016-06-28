# telepy
A simple,intuitive telegram bot made for interaction and data fetching from Raspberry pi.Currently this ChatBot is hotsted on Microsoft Azure for prompt and lag free responses.You can access the demo @https://telegram.me/nsniteshsahni_bot 

# Examples
To interact with bot,you can reference following examples

```
/hi
```
To greet your device


```
/wiki Delhi
```
It will perform a wikipedia search and retunrs the relevant data without any clutter

```
/torrent <magnet link/torrent URL/info hash>
```
Adds and downloads torrent remotely toy your device.Uses deluge torrent client as backend.
Visit above bot URL for more interesting features and commands.
# Requirements  
This bot requires following Python librarires:
- Wikipedia
- OpenWeatherMap
- Python wrapper class for telegram

# Installation
```
sudo pip install wikipedia
sudo pip install pyowm
sudo pip install telepot
sudo pip install pyshorteners
sudo apt-get install deluge
```
Install deluge torrent client fore torrent downloading feature.
Now just simply run bot.py and attach it to startup process for uninterrupted operation

# API Reference
1. Wikipedia for data fetching
2. OpenWeatherMaps for weather details
3. GPIO Library for python
4. Telegram API for bot
5. Google API for URL Shortening
6. Deluge Console API for remote torrent downloading

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
