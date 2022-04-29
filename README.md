# SmashBot
SmashBot is a script that creates a virtual controller that can spam keys. It's useful to practice true combos in Yuzu, because the built-in Smash combo counter isn't reliable for true combos.
![smashbot](https://user-images.githubusercontent.com/29168302/165932288-d9ade949-e665-4acc-95d2-4666734d4419.gif)
## WINDOWS ONLY!

## Installation
 - Install venv (if you don't have it installed)
`(path-to-python) -m pip install --user virtualenv`

 - Create venv in project directory 
`cd smashbot`
`py -m venv env`

 - Activate venv
`.\env\Scripts\activate`

 - Install requirements
`pip install -r requirements.txt`
This will also install ViGEmBus, follow interactive installer.

## Usage
 - Make sure you're in an activated virtual env.
 - Basic usage (to spam shield) is:
`python smashbot.py -s`
 - After the script is running, open Yuzu, go to 'Emulation'>'Configure...'>'Controls', go to 'Player 2' and make sure the input device is mapped to 'DualShock 4 Controller 0'.
