from os import path, remove
from time import sleep
import os

from driver_builder import DriverBuilder

from selenium import webdriver  
from selenium.webdriver.chrome import webdriver as chrome_webdriver
from selenium.webdriver import Chrome

class RMPDownload:
    def download(self,equipment):

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

        driver.get("http://rmp.global.schindler.com/Equipment/EquipmentMain/EquipmentDetails/?sapSys=ZAP&equnr="+equipment) 

        try :
            js = ''' document.querySelectorAll("li")[36].click();

              
            '''
            driver.execute_script(js)
        except: 
            print("exception 1 ")

        sleep(5)  
 
        try :
            js = ''' document.getElementById('ExportWithParameters1').click(); '''
            driver.execute_script(js)
        except:
            print("exception 2 ")

        self.wait_until_file_exists(equipment+"_MessagesExport_", 20)

        try :
            js = ''' document.querySelectorAll("li")[35].click();

 '''
            driver.execute_script(js)
        except: 
            print("exception 3 ")

        sleep(5)  
 
        try :
            js = ''' document.getElementById('EventExportButton').click(); '''
            driver.execute_script(js)
        except:
            print("exception 4 ")

        self.wait_until_file_exists(equipment+"_EventsExport_", 20)
        driver.close()

        print("done")

    def wait_until_file_exists(self, actual_file, wait_time_in_seconds=5):
        waits = 0
        path="./"
                      
        while waits < wait_time_in_seconds:
            fileList=os.listdir(path)
            for file in fileList:
               print("file name=",file)
               if file.find(actual_file) >=0 :
                    return 

            print("sleeping...." + str(waits))
            sleep(.5)  # make sure file completes downloading
            waits += .5




if __name__ == "__main__":
 
    print("testing download")
    path_root="./"

    fileList=os.listdir(path_root)
    for file in fileList:
        print("file name=",file)
        if file.find("10000021") >=0 :
            os.remove(path+file)


    t=RMPDownload()
    t.download("10000021")












