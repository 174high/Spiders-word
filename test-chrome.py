import pychrome
from bs4 import BeautifulSoup
import requests


# create a browser instance
browser = pychrome.Browser(url="http://127.0.0.1:9222")

# create a tab
tab = browser.new_tab()

# register callback if you want
def request_will_be_sent(**kwargs):
    print("loading: %s" % kwargs.get('request').get('url'))

tab.Network.requestWillBeSent = request_will_be_sent

# start the tab 
tab.start()

# call method
tab.Network.enable()
# call method with timeout
#tab.Page.navigate(url="http://rmp.global.schindler.com/Equipment/EquipmentMain/EquipmentDetails/?sapSys=ZAP&equnr=10000021", _timeout=5)

tab.call_method('Page.navigate',url="http://rmp.global.schindler.com/Equipment/EquipmentMain/EquipmentDetails/?sapSys=ZAP&equnr=10000021", _timeout=5)

# wait for loading
tab.wait(2)

html = tab.Runtime.evaluate(expression="document.documentElement.outerHTML")

soup = BeautifulSoup(((html['result'])['value']),"html.parser")

#print(soup)
print(soup.select("#GatewayType"))
print(soup.title)

# stop the tab (stop handle events and stop recv message from chrome)
tab.stop()

# close tab
browser.close_tab(tab)





















