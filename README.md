prerequisite : Python 3.7.3 Anaconda  Qt Designer   pychrome  Anaconda   Beautiful Soup(�����)
 
--------------------------------------------------------------------------------------------
(https://stackoverflow.com/questions/8921188/issue-with-virtualenv-cannot-activate)
���л���
1.  Anaconda Prompt(window Ӧ�ó���) 

2.  ��װ virtualenv(�Ѿ���װ�Ĳ���,����ʹ����Ѹ��ĵ��ԣ�����ѡ�����⻷�������Ա���ÿ�ΰ�װ�³�����������Ȩ��) 
pip install -U pip virtualenv

3.  ����
virtualenv --system-site-packages -p python ./venv  

4.  ����
 .\venv\Scripts\activate 

-----------------------------------------------------------------------------------------------
Ϊʲôʹ�� pychrome 

(https://blog.csdn.net/g8433373/article/details/79833471)
�����ս��� Chrome Headless
���
�Դ�Google�ٷ�������Chrome�����������̬ģʽ֮��,PhantomJS ά���� Vitaly Slobodin �漴���ʼ��б���������ְ,�ɼ���ģʽ��Ӱ��������ô����С�����ҿ����������ʹ�øü���ʵ������ץȡ������˵�������׼����ܹ�Ӧ��90%����վ,�Ӵ�����0�ż���

-------------------------------------------------------------------------------------------------

1. (https://www.jianshu.com/p/5b063c5745d0) ���ʹ�� Qt Designer   
ʹ��  Qt Designer  ��ͼ
���� designer 

2. ����
ui-FormMonitor.ui

3. ��ʹ��pyuic5�� uiת��Ϊ py ����  
pyuic5 -o  Ui_FormMonitor.py  Ui_FormMonitor.ui 

4. python  Ui_FormMonitor.py ���Կ������ɵ�Ч��(��Ҫ��� main ����)

--------------------------------------------------------------------------------------------------

(https://github.com/fate0/pychrome)  ������� pychrome 
1. how to install pychrome    //��װpychrome  

$ pip install -U pychrome
or from GitHub:

$ pip install -U git+https://github.com/fate0/pychrome.git

or from source:
$ python setup.py install

2.  Setup Chrome              // ����chrome,����֮ǰ��Ҫ�ر��������е�chrome  
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






















