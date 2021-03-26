pushd .
cd ..
call venv\Scripts\activate.bat 
mypy -m tobool
call deactivate
popd
