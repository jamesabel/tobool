set PYTHONPATH=%CD%
venv\Scripts\pytest.exe --rootdir="." -s test_tobool --cov-report xml:coverage.xml --cov=.\
set PYTHONPATH=
