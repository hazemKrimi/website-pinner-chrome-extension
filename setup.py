import PyInstaller.__main__
import os

PyInstaller.__main__.run(['--onefile', '--noconsole', os.path.join('main.py')])