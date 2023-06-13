# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
from pathlib import Path

import catkin_pkg.package

# -- Retrieve package version ------------------------------------------------
catkin_dir = Path(__file__).joinpath("../../..").resolve()
catkin_package = catkin_pkg.package.parse_package(
    catkin_dir.joinpath(catkin_pkg.package.PACKAGE_MANIFEST_FILENAME)
)

project = 'test_pkg'
copyright = '2023, Rick Staa'
author = 'Rick Staa'
release = catkin_package.version
version = ".".join(release.split(".")[:3])

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "autoapi.extension",  # Generate API documentation from code.
]
autoapi_dirs = [
    "../../src/test_pkg",
    str(
        catkin_dir.joinpath(
            "../../devel/lib/python3/dist-packages/test_pkg"
        ).resolve()
    ),
]
autoapi_member_order = "bysource"

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
