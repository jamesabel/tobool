pushd .
cd ..
call venv\Scripts\activate.bat 
REM target the oldest Python version mypy still supports, since CI tests older versions than the local venv runs
mypy --python-version 3.10 -m tobool
call deactivate
popd
