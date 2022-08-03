python -m pip install pystyle
python -m pip install requests
python -m pip install os
python -m pip install shutil
python -m pip install colorama
python -m pip install json

cls
echo python palion.py >> start.bat
start start.bat
start /b "" cmd /c del "%~f0"&exit /b