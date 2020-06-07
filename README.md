# Python ScreenPlay example

![](../../workflows/Run%20tests/badge.svg)

[Linux instructions](#Linux)

[Windows instructions](#Windows)

---

## Linux

### Setup and installing requirements

1. Download `chromedriver` and make sure it's in your path.
   The latest version can be downloaded from
   [here](https://chromedriver.chromium.org/downloads).

2. Creating a python virtual environment
   ``` shell
   $ ./create_virtual_environment.sh
   ```

3. Install the python requirements
   ``` shell
   $ ./install_requirements.sh
   ```

### Running the tests

1. Enter the virtual environment (if you're not already in it)
   ``` shell
   $ source .venv/bin/activate
   ```

2. Run the tests
   ``` shell
   (.venv) $ behave
   ```

---

## Windows

### Setup and installing requirements

1. Creating a python virtual environment
   ``` cmd
   > create_virtual_environment.bat
   ```

2. Install the python requirements
   ``` cmd
   > install_requirements.bat
   ```

### Running the tests

1. Enter the virtual environment (if you're not already in it)
   ``` cmd
   > .venv\Scripts\activate.bat
   ```

2. Run the tests
   ``` cmd
   (.venv) > behave
   ```
