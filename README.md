prerequisite : Python 3.7.3 Anaconda  Qt Designer   pychrome  Anaconda   Beautiful Soup(爬虫库)
 
--------------------------------------------------------------------------------------------
(https://stackoverflow.com/questions/8921188/issue-with-virtualenv-cannot-activate)
运行环境
1.  Anaconda Prompt(window 应用程序) 

2.  安装 virtualenv(已经安装的不用,由于使用了迅达的电脑，所以选择虚拟环境，可以避免每次安装新程序都申请运行权限) 
pip install -U pip virtualenv

3.  配置
virtualenv --system-site-packages -p python ./venv  

4.  激活
 .\venv\Scripts\activate 

-----------------------------------------------------------------------------------------------
为什么使用 pychrome 

(https://blog.csdn.net/g8433373/article/details/79833471)
爬虫终结者 Chrome Headless
简介
自从Google官方发布了Chrome浏览器的无形态模式之后,PhantomJS 维护者 Vitaly Slobodin 随即在邮件列表上宣布辞职,可见该模式的影响力，那么下面小编带大家快速入门如何使用该技术实现数据抓取，可以说掌握这套技术能够应对90%的网站,从此爬虫0门槛。

-------------------------------------------------------------------------------------------------

1. (https://www.jianshu.com/p/5b063c5745d0) 如何使用 Qt Designer   
使用  Qt Designer  画图
运行 designer 

2. 生成
ui-FormMonitor.ui

3. 再使用pyuic5把 ui转化为 py 程序。  
pyuic5 -o  Ui_FormMonitor.py  Ui_FormMonitor.ui 

4. python  Ui_FormMonitor.py 可以看到生成的效果(需要添加 main 函数)

--------------------------------------------------------------------------------------------------

(https://github.com/fate0/pychrome)  如何入门 pychrome 
1. how to install pychrome    //安装pychrome  

$ pip install -U pychrome
or from GitHub:

$ pip install -U git+https://github.com/fate0/pychrome.git

or from source:
$ python setup.py install

2.  Setup Chrome              // 运行chrome,运行之前需要关闭正在运行的chrome  
simply:

$ google-chrome --remote-debugging-port=9222

or headless mode (chrome version >= 59):
$ google-chrome --headless --disable-gpu --remote-debugging-port=9222


3. run test program 

python Remote-Monitoring-Platform.py

-----------------------------------------------------------------------------------------------------
genarate a ***.exe 


pyinstaller --noconsole   Remote-Monitoring-Platform.py  //without a console 

pyinstaller   Remote-Monitoring-Platform.py              //there is a console in programe to debug 
  
pyinstaller --noconsole  --ico="name .ico"  Remote-Monitoring-Platform.py  // creat an icon we need 

----------------------------------------------------------------
4. run map service for rmp 

npm run serve






















