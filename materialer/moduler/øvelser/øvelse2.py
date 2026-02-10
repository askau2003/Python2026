import subprocess
import os


subprocess.run(['git','clone','https://github.com/python-elective-kea/spring2024'])

os.chdir('spring2024')
os.chdir('docs')
os.startfile('index.html')
