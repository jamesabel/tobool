echo on
py -3.14 -m venv --clear venv
if errorlevel 1 exit /b 1
call venv\Scripts\activate.bat
python -m pip install --no-deps --upgrade pip
python -m pip install -U setuptools
python -m pip install -U -r requirements-dev.txt
call deactivate
