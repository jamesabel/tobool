pushd .
cd ..
call build.bat
call venv\scripts\activate.bat
twine upload dist\*
call deactivate
popd
