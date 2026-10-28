# Calculator with PyBuilder

This Lab 6 calculator implements addition, subtraction, multiplication, division,
modulus, exponentiation, and square root. PyBuilder runs its 15 unit tests and
creates installable distribution packages.

## Setup

Run these commands from this directory with Python 3.12:

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, activate the environment with `.venv\Scripts\activate`.

## Test and build

```sh
# Run the calculator tests.
pyb run_unit_tests

# Clean, test, and build the distribution packages.
pyb clean publish

# Run the default workflow, which also tests and packages the calculator.
pyb

# Run the tests directly, as specified in the lab.
python -m unittest tests.unittest.calculator_Karim_Abdallah.test_calculator_Karim_Abdallah
```

The `publish` task creates files locally. Uploading to a package registry is a
separate operation.

## Distribution packages

Generated packages are under
`target/dist/calculator_Karim_Abdallah-0.1/dist/`:

- `calculator_karim_abdallah-0.1-py3-none-any.whl`: an installable wheel containing
  the calculator module and package metadata.
- `calculator_karim_abdallah-0.1.tar.gz`: a source distribution that can be used
  to build and install the calculator.

For example, install the wheel with:

```sh
python -m pip install target/dist/calculator_Karim_Abdallah-0.1/dist/calculator_karim_abdallah-0.1-py3-none-any.whl
```

`build.py` configures PyBuilder. `pyproject.toml` tells standard Python build
tools to use PyBuilder. The root `setup.py` is PyBuilder's generated compatibility
script; use `pyb` or `python -m pip install .` to build or install the project.
Generated output and virtual environments are excluded from Git.
