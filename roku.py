import requests
import xml.etree.ElementTree as ET
from colorama import Fore,Style

print("\033[1m" + Fore.BLUE + 'Welcome to the Roku remote!\n' + Style.RESET_ALL)
ip = input('Enter the IP address of your device: ')
port = input('Enter the port number (default is 8060): ') or "8060"
URL = f'http://{ip}:{port}'

print('Checking to see if your device is online...')
response = requests.get(URL + '/query/device-info')

if response.status_code == 200:
    print('Device is online!\n')

    while True:
        print('\nChoose what you would like the remote to do:')
        print('0. Power On')
        print('1. Keypad Up')
        print('2. Keypad Down')
        print('3. Keypad Left')
        print('4. Keypad Right')
        print('5. Go Home')
        print('6. Select')
        print('7. Back')
        print('8. Volume Up')
        print('9. Volume Down')
        print('10. List Apps')
        print('11. Launch App')
        print('12. Exit')

        select = input('Enter your selection: ')

        commands = {
            '1': 'Up',
            '2': 'Down',
            '3': 'Left',
            '4': 'Right',
            '5': 'Home',
            '6': 'Select',
            '7': 'Back',
            '8': 'VolumeUp',
            '9': 'VolumeDown',
            '0': 'PowerOn'
        }

        if select in commands:
            req_response = requests.post(URL + f'/keypress/{commands[select]}')
            if req_response.status_code == 200:
                print(f"Sent '{commands[select]}' command!")
            else:
                print(f'Error: {req_response.status_code}')

        elif select == '10':  # List installed apps
            apps_response = requests.get(URL + '/query/apps')
            if apps_response.status_code == 200:
                root = ET.fromstring(apps_response.content)
                print("\nInstalled Apps:")
                apps = {}
                for app in root.findall('app'):
                    print(f"{app.text} (ID: {app.attrib['id']})")
                    apps[app.text.lower()] = app.attrib['id']
            else:
                print('Failed to retrieve apps.')

        elif select == '11':  # Launch an app
            app_name = input("Enter the app name (case-insensitive): ").strip().lower()
            apps_response = requests.get(URL + '/query/apps')
            if apps_response.status_code == 200:
                root = ET.fromstring(apps_response.content)
                apps = {app.text.lower(): app.attrib['id'] for app in root.findall('app')}

                if app_name in apps:
                    app_id = apps[app_name]
                    launch_response = requests.post(URL + f'/launch/{app_id}')
                    if launch_response.status_code == 200:
                        print(f"Launching {app_name}...")
                    else:
                        print(f"Failed to launch {app_name} (Error {launch_response.status_code})")
                else:
                    print("App not found. Try listing apps first.")
            else:
                print('Failed to retrieve apps.')

        elif select == '12':  # Exit
            print("Exiting remote control. Goodbye!")
            break

        else:
            print('Invalid selection, please try again.')

else:
    print(f'Error: Device not reachable (status code {response.status_code}).')
