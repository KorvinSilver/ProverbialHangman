# PySide Instructions

PySide is an abandoned project licensed under [LGPL 2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html) that provides Python with Qt4 bindings.
It supports Python up to version 3.4, but technically it works with Python 3.6.<br>
I've built a wheel package for Linux x86_64 and Python 3.6. You can [download it from here](https://drive.google.com/uc?id=1gvZsU2Y2-YX6mGOsd1INwp6ZC-vxDRPE&export=download).

For PySide2, visit https://wiki.qt.io/PySide2

##### Here's how to build and install your own PySide 1.2.4 on Linux using Python 3.6 and pip (of course there's no guarantee it'll work):

- First make sure Qt4 is installed. For that, refer to your operating system's manual.

- Open a terminal in the `ProverbialHangman` directory

- Optionally create a Python virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    - To leave the venv when you don't need it anymore, call the command `deactivate`
    - For more about virtual environments, visit https://docs.python.org/3/library/venv.html

- Download and extract PySide 1.2.4:

    ```bash
    wget https://pypi.python.org/packages/source/P/PySide/PySide-1.2.4.tar.gz
    tar xfz PySide-1.2.4.tar.gz
    cd PySide-1.2.4
    ```

- In file `setup.py` find the following line (the spaces are not a mistake, the line is indented):

    ```
            'Programming Language :: Python :: 3.4',
    ```

- and add this line after it (including the indentation):

    ```
            'Programming Language :: Python :: 3.6',
    ```

- In file `PKG-INFO` find the following line:

    ```
    Classifier: Programming Language :: Python :: 3.4
    ```

- and add this line after it:

    ```
    Classifier: Programming Language :: Python :: 3.6
    ```

- Continue with the build and install (could take a long time depending on your computer):

    ```bash
    python3 setup.py bdist_wheel --qmake=/usr/bin/qmake-qt4 --standalone --jobs=8
    cd dist
    pip3 install --no-index PySide-1.2.4-*.whl
    ```

The steps should be the same for 3.5, 3.7 and future Python versions, only replace 3.6 with the version you use.
