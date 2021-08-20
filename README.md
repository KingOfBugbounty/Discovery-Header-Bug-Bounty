<h1 align="center"> 👑 Discovery Header DoD Bug-Bounty </h1> 



Did you know that DoD accepts server headers? 😲 (example: apache"version" , php"version") ?

In this code it is possible to extract all headers from the URLS. 
Tracking versions and being able to report as cwe-200 on hackerone.

the 200dds file is an example:

You can put your list of treated URLS.

[![asciicast](https://asciinema.org/a/g2kPiCA0qwVHImPsfFCIClzm8.svg)](https://asciinema.org/a/g2kPiCA0qwVHImPsfFCIClzm8)


### Install dependencies

```bash
git clone https://github.com/KingOfBugbounty/Discovery-Header-Bug-Bounty.git

cd Discovery-Header-Bug-Bounty

pip install -r requirements.txt

python3 searchHEADER.py -h

usage: searchHEADER.py [-h] help

positional arguments:
  help        Run to code = python3 searchHEADER.py FileToUrls

optional arguments:
  -h, --help  show this help message and exit


```

# Project

[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)
[![Telegram](https://patrolavia.github.io/telegram-badge/chat.png)](https://t.me/KingOfTipsBugBounty)


<a href="https://www.buymeacoffee.com/OFJAAAH" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 20px !important;width: 50px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
