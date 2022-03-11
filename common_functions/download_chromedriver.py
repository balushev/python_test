# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 17:30:36 2021

@author: bbalushev
"""


import os
import zipfile
import requests
import wget
from win32com.client import Dispatch


class GetChromedriver:
    """ GetChromedriver class provide methods which checks what Chrome version is installed
        and downloads the required Chromedriver
    """

    # ================================ Initialization method ================================
    def __init__(self, location: str = '') -> None:

        """ Constructor method

            Method parameters:
                location -> can contain '' or some specific location of chrome.exe

            Return value -> None

        """

        self.locations = ['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
                          'C:\Program Files\Google\Chrome\Application\chrome.exe']
        if location != '':
            self.locations.append(location)
        self.full_version = ''

    # ================================ Get Chrome version method ================================
    def get_local_chrome_version(self) -> str:
        """ get_local_chrome_version method returns the version of the installed Chrome

            Method parameters -> None
            Return value -> version of chrome local installation

        """

        parser = Dispatch("Scripting.FileSystemObject")
        for item in self.locations:
            if os.path.isfile(item):
                self.full_version = parser.GetFileVersion(item)
        local_version_number = self.full_version.split(".")[0]
        return local_version_number

    # =========================== Get required Chromedriver version method ===========================
    def get_required_chromedriver_version_release_number(self) -> str:
        """ get_required_chromedriver_version_release_number method returns the full version
            of the required chromedriver

            Method parameters -> None

            Return value -> required chromedriver version

        """

        url = f'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{self.get_local_chrome_version()}'
        response = requests.get(url)
        required_version_number = response.text
        return required_version_number

    # ============================= Chromedriver download url method =============================
    def create_required_chromedriver_download_url(self) -> str:
        """ create_required_chromedriver_download_url method returns the full url
            for the download of the required chromedriver

            Method parameters -> None

            Return value -> required chromedriver url

         """

        version_release_number = self.get_required_chromedriver_version_release_number()
        print(f"===> Downloading chromedriver version {version_release_number}")

        return f"https://chromedriver.storage.googleapis.com/{version_release_number}/chromedriver_win32.zip"

    # ================================ Download Chromedriver method ================================
    def download_chromedriver(self) -> None:
        """ download_chromedriver method downloads the required chromedriver and unzipped it  in 'drivers' folder

            Method parameters -> None
            Return value -> None

        """

        latest_driver_zip = wget.download(self.create_required_chromedriver_download_url(), 'chromedriver.zip')
        with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
            zip_ref.extractall('drivers')
        os.remove(latest_driver_zip)

    # ================================ Driver discrepancy check method ================================
    def check_chromedriver_chrome_discrepancy(self) -> None:
        """ check_chromedriver_chrome_discrepancy method checks if correct chromedriver is present
            and if not, downloads the required chromedriver

            Method parameters -> None
            Return value -> None

        """

        chrome_version = self.get_local_chrome_version()
        with open('drivers/drivers version/chromedriver_version.txt', 'r') as file:
            chromedriver_version = file.read()
        if chrome_version != chromedriver_version:
            print(f"===> Chromedriver version {chromedriver_version} is not compatible with"
                  f" Chrome version {chrome_version}, downloading correct version!")
            self.download_chromedriver()
