**Virtual Environment**
A virtual environment in Python is an isolated environment on your computer, where you can run and test your Python projects.
It allows you to manage project-specific dependencies without interfering with other projects or the original Python installation.
It also have many features like:
Has its own Python interpreter
Has its own set of installed packages
Is isolated from other virtual environments
Can have different versions of the same package
Using virtual environments is important because:
It prevents package version conflicts between projects
Makes projects more portable and reproducible
Keeps your system Python installation clean
Allows testing with different Python versions
**Creating a Virtual Environment**
Python has the built-in venv module for creating virtual environments.
I used  **python -m venv first_venv** command to generate v-env withing my 11\9\26 folder, by chaning the path to that particular directory. After creating a venv, it install these files Include/ → contains C/C++ header files that some Python packages may need.
Lib/ → contains the Python packages installed inside your virtual environment.
Scripts/ → contains executables such as python, pip, and the activation scripts.
pyvenv.cfg → configuration file telling Python that this folder is a virtual environment and which base Python installation it uses.
.gitignore → tells Git which files/folders it should not upload to GitHub.