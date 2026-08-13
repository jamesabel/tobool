# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

`tobool` is a small, dependency-free Python library published to PyPI. It converts many representations of a boolean (strings like "yes"/"off", ints, Decimals, None) to an actual `bool` or `None`. Development is Windows-centric: tooling is driven by `.bat` scripts and a local `venv\` directory.

## Commands

Environment setup (creates `venv\` from a system Python and installs `requirements-dev.txt`):

```
make_venv.bat
```

Run tests with coverage (from the repo root):

```
pytest.bat
```

Run a single test directly:

```
venv\Scripts\pytest.exe -s test_tobool\test_to_bool.py::test_strict
```

Lint/format/type-check — these scripts resolve paths relative to the parent of the current directory (`cd ..`), so they MUST be run from inside the `scripts\` directory:

- `blackify.bat` — black with line length 192 (`-l 192`) over `tobool` and `test_tobool`
- `run_flake8.bat` — flake8 (ignores E402,F401,W503,E203,E501; report written to `doc\flake8_report.txt`)
- `run_mypy.bat` — mypy on the `tobool` module (the package ships `py.typed`)

Build a wheel: `build.bat` (run from the repo root). Publish to PyPI: `pypi.bat` (run from inside `scripts\`; calls build then twine).

CI (GitHub Actions, `.github/workflows/python-package.yml`) runs flake8 and `pytest test_tobool` on Python 3.8–3.15, so keep the code compatible with older Pythons despite the local venv being newer.

## Architecture

All library code is in a single module, `tobool/tobool.py`, re-exported via `tobool/__init__.py`:

- `to_bool(value)` — the core conversion; returns `bool` or `None`, raises `ValueError` for anything unrecognized. Missing-value representations (`None`, NaN, and strings like "none"/"null"/"nil"/"na"/"nan"/"n/a"/"undefined"/"") map to `None`. Any `numbers.Number` equal to 0 or 1 converts; bytes are decoded and treated as strings; numeric strings like "1.0" convert via float. String vocabulary handling is a vendored-and-extended copy of the removed `distutils.util.strtobool`. Internationalization (e.g. "si") is deliberately out of scope.
- `to_bool_strict(value, fault_on_none=False)` — wraps `to_bool` but always returns a `bool`; `None` becomes `False`, or raises `ToBoolNoneValueException` when `fault_on_none=True`.
- All three functions are decorated with `@lru_cache()`, so inputs must remain hashable.

Package metadata (`__version__`, author, URLs) lives in `tobool/__version__.py` and is imported by `setup.py` — bump the version there for releases.

Tests in `test_tobool/test_to_bool.py` are table-driven from a `test_values` dict mapping expected results (`False`/`True`/`None`) to input variants; add new supported representations to those tables rather than writing new one-off tests.
