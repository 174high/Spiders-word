import subprocess


subprocess.call("python run_chrome.py", shell=True)
subprocess.call('''pyinstaller  --noconsole   --ico="name .ico"  Remote-Monitoring-Platform.py''', shell=True)
#subprocess.call('''pyinstaller --noconsole   --ico="name .ico"  Remote-Monitoring-Platform.py''', shell=True)
subprocess.call("pyinstaller  --noconsole    excel.py", shell=True)
#subprocess.call("pyinstaller excel.py", shell=True)

subprocess.call("cp -r  device-log dist/Remote-Monitoring-Platform/", shell=True)
subprocess.call("cp -r  device-event dist/Remote-Monitoring-Platform/", shell=True)
subprocess.call("cp -r   dist/excel/excel.exe  dist/Remote-Monitoring-Platform/", shell=True)
subprocess.call("cd dist/Remote-Monitoring-Platform/  & md result", shell=True)
subprocess.call("cd dist/Remote-Monitoring-Platform/  & md device-file", shell=True)
subprocess.call("cp -r  'Field Problem Feedback-Template.docx'  dist/Remote-Monitoring-Platform/device-file", shell=True)
subprocess.call("cp -r  'rmp info-Template.docx' dist/Remote-Monitoring-Platform/device-file", shell=True)
subprocess.call("cp -r  PythonHeadlessChrome/drivers  dist/Remote-Monitoring-Platform/", shell=True)