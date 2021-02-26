echo on
rmdir /S /Q venv
"\Program Files\Python38\python.exe" -m venv --clear venv
call venv\Scripts\activate.bat
python -m pip install --no-deps --upgrade pip
pip3 install -U setuptools
pip3 install -U -r requirements-dev.txt
call deactivate
