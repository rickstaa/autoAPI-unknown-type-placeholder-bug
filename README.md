# AutoAPI Unknown Type Placeholder Bug

> **Warning**
> A newer more simple example repository is found in https://github.com/rickstaa/unknown_type_placeholder_bug/blob/main/README.md.

This is a simple example repository to demonstrate the `WARNING: Unknown type: placeholder` bug that is thrown in
AutoAPI when using it within a ROS package (see https://github.com/readthedocs/sphinx-autoapi/issues/180).

## Steps to Reproduce

1.  Install ROS Noetic (http://wiki.ros.org/noetic/Installation/Ubuntu).
2.  Install Python 3.8 (https://docs.python.org/3/).
3.  Create a catkin workspace (http://wiki.ros.org/catkin/Tutorials/create\_a\_workspace).
4.  Install the ros dependencies (i.e. `rosdep install --from-paths src --ignore-src -r -y`).
5.  Install the venv python package (i.e. `sudo apt install python3-venv`).
6.  Create a new virtual environment using the `--system-site-packages` flag (i.e. `python3 -m venv test_pkg --system-site-packages`).
7.  Build the catkin workspace (i.e. `catkin build`).
8.  Install the python dependencies (i.e. `pip install -r requirements/doc_requirements.txt`).
9.  Build the documentation from within the `docs` folder (i.e. `make html`).
10. Be greeted by the `WARNING: Unknown type: placeholder` bug.
