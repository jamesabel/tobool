call local_install.bat
set PYTHONPATH=%CD%
venv\Scripts\pytest.exe --rootdir="." -s test_tobool
set PYTHONPATH=
