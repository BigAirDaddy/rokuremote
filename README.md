# Roku Remote
# Roku Remote Control Script

## Overview
This Python script allows you to control your Roku device remotely using its external control API. You can navigate the Roku interface, control volume, list installed apps, launch apps, and manage playback directly from the terminal.

## Features
- Power on/off the Roku device
- Navigate using arrow keys
- Go home, select, and go back
- Adjust volume and mute
- Control media playback (play/pause, rewind, fast forward)
- Display media information
- List installed apps
- Launch an app by name

## Prerequisites
- A Roku device connected to the same network as your computer
- Python 3 installed
- Required Python libraries:
  - `requests`
  - `colorama`
  
## Installation
1. Clone or download this repository.
2. Install dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the script:
   ```bash
   python roku_remote.py
   ```
2. Enter the Roku device's IP address and port (default: 8060).
3. Select an option from the menu to control the device.

## Command Menu
| Option | Function |
|--------|----------|
| 0 | Power On |
| 1 | Keypad Up |
| 2 | Keypad Down |
| 3 | Keypad Left |
| 4 | Keypad Right |
| 5 | Go Home |
| 6 | Select |
| 7 | Back |
| 8 | Volume Up |
| 9 | Volume Down |
| 10 | List Apps |
| 11 | Launch App |
| 12 | Play/Pause |
| 13 | Rewind |
| 14 | Fast Forward |
| 15 | Info |
| 16 | Mute |
| 17 | Power Off |
| 18 | Exit |

## Notes
- Ensure your Roku device allows external control under **Settings > System > Advanced System Settings > External Control > Enable Control via Network**.
- If an app launch fails, check that the app name matches exactly (case-insensitive).
- Play/Pause, Rewind, and Fast Forward work during media playback.
- Power Off is supported only on some Roku models.

## License
This project is open-source and available under the MIT License.




