from os import path, remove
from time import sleep
import os

from driver_builder import DriverBuilder

from selenium import webdriver  
from selenium.webdriver.chrome import webdriver as chrome_webdriver
from selenium.webdriver import Chrome

class TestDownload:
    def test_download(self):

        driver_builder = DriverBuilder()
        download_path = path.dirname(path.realpath(__file__))
        expected_download = path.join(download_path, "5MB.zip")

        print("download_path=",download_path)
        print("expected_download=",expected_download)

        # clean downloaded file
        try:
            remove(expected_download)
        except OSError:
            pass

        assert (not path.isfile(expected_download))

        driver = driver_builder.get_driver(download_path, headless=True)

        driver.get("http://rmp.global.schindler.com/Equipment/EquipmentMain/EquipmentDetails/?sapSys=ZAP&equnr=10000021") 

        print("title of baidu=",driver.title)
 
        print("url =",driver.current_url)

        try :
            js = ''' document.querySelectorAll("li")[36].click();

              
            '''
            driver.execute_script(js)
        except: 
            print("exception")

        sleep(5)  
 
        try :
            js = ''' document.getElementById('ExportWithParameters1').click(); '''
            driver.execute_script(js)
        except:
            print("exception")

        self.wait_until_file_exists(expected_download, 600)
        driver.close()

        assert (path.isfile(expected_download))

        print("done")

    def wait_until_file_exists(self, actual_file, wait_time_in_seconds=5):
        waits = 0
        while not path.isfile(actual_file) and waits < wait_time_in_seconds:
            print("sleeping...." + str(waits))
            sleep(.5)  # make sure file completes downloading
            waits += .5


if __name__ == "__main__":
 
    print("testing download")
    t=TestDownload()
    t.test_download()
