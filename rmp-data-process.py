import pychrome
from bs4 import BeautifulSoup
import requests


# create a browser instance
browser = pychrome.Browser(url="http://127.0.0.1:9235")


# create a tab
tab = browser.new_tab()


# register callback if you want
#def request_will_be_sent(**kwargs):
#    print("loading: %s" % kwargs.get('request').get('url'))

#tab.Network.requestWillBeSent = request_will_be_sent


# start the tab 
tab.start()

# call method
tab.Network.enable()

# call method with timeout
#tab.Page.navigate(url="http://rmp.global.schindler.com/Equipment/EquipmentMain/EquipmentDetails/?sapSys=ZAP&equnr=10000021", _timeout=5)

#tab.call_method('Page.navigate',url="https://mirrors.edge.kernel.org/pub/", _timeout=5)

tab.call_method('Page.navigate',url="http://rmp.global.schindler.com/Monitoring/WatchList", _timeout=5)

#tab.call_method('Page.navigate',url="https://movie.douban.com/subject/26260853/comments?start=0&amp;limit=20&amp;sort=new_score&amp;status=P", _timeout=5)

# wait for loading
tab.wait(2)


html = tab.Runtime.evaluate(expression="document.documentElement.outerHTML")

#print(html)

soup = BeautifulSoup(((html['result'])['value']),"html.parser")

#for link in soup.find_all(class_="k-list-optionlabel k-state-selected k-state-focused"):
#    print(link)

#for link in soup.find_all(class_="k-item",role="option"):
#    print(link)

for link in soup.find_all('a'):
        if link.get('href').find("equnr=") > 0 :
            print(link.get('href')[link.get('href').find("equnr=")+6:])
             #print(link)

cmd='''
var myFunction = function () {
    
    $(".k-icon.k-i-arrow-60-right").trigger('click')
}
myFunction();

'''

#print(cmd)
tab.Runtime.evaluate(expression=cmd)

tab.wait(2)

html = tab.Runtime.evaluate(expression="document.documentElement.outerHTML")

#print(html)

soup = BeautifulSoup(((html['result'])['value']),"html.parser")

#for link in soup.find_all(class_="k-list-optionlabel k-state-selected k-state-focused"):
#    print(link)

#for link in soup.find_all(class_="k-item",role="option"):
#    print(link)

for link in soup.find_all('a'):
        if link.get('href').find("equnr=") > 0 :
            print(link.get('href')[link.get('href').find("equnr=")+6:])
             #print(link)


# stop the tab (stop handle events and stop recv message from chrome)
tab.stop()

# close tab
browser.close_tab(tab)


















