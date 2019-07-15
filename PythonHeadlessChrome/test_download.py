from os import path, remove
from time import sleep

from driver_builder import DriverBuilder


class TestDownload:
    def test_download(self):

        driver_builder = DriverBuilder()

        download_path = path.dirname(path.realpath(__file__))

        print("download path=",download_path )

        expected_download = path.join(download_path, "5MB.zip")

        print("expected_download=",expected_download )

        # clean downloaded file
        try:
            remove(expected_download)
        except OSError:
            pass

        assert (not path.isfile(expected_download))

        driver = driver_builder.get_driver(download_path, headless=True)

        driver.get("https://www.thinkbroadband.com/download")

#        driver.get("http://rmp.global.schindler.com/Equipment/EquipmentMain/EquipmentDetails/?sapSys=ZAP&equnr=10000021")

#        driver.get("https://hamupp.github.io/gitblog/app/jsBasic/jsButtonDownloadFile/index.html")

        clone_box = driver.find_element_by_xpath('//*[@id="main-col"]/div/div/div[8]/p[1]/a/img')
#        clone_box =driver.find_element_by_id('#ExportWithParameters1')

#        clone_box =driver.find_element_by_id('btn1')

#        clone_box =driver.find_element_by_partial_link_text('chromedriver')
        clone_box.click()

        self.wait_until_file_exists(expected_download, 30)
        driver.close()

        assert (path.isfile(expected_download))

        print("done")

    def wait_until_file_exists(self, actual_file, wait_time_in_seconds=5):
        waits = 0
        while not path.isfile(actual_file) and waits < wait_time_in_seconds:
            print("sleeping...." + str(waits))
            sleep(.5)  # make sure file completes downloading
            waits += .5

print("testing download")
t=TestDownload()
t.test_download()




