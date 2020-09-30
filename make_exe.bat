@ echo Install dependency
@ pip install -r requirements.txt
@ echo Install pyinstaller
@ python -m pip install -U pyinstaller
@ echo Build exe
@ pyinstaller --onefile --add-binary "chromedriver.exe";"." script.py -i appicon.ico
@ echo Successfully build exe