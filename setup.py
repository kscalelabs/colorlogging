# mypy: disable-error-code="import-untyped"
#!/usr/bin/env python
"""Setup script for the project."""

import re

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description: str = f.read()

requirements = []
requirements_dev = ["black", "darglint", "ruff", "mypy", "pytest"]

with open("colorlogging/__init__.py", "r", encoding="utf-8") as fh:
    version_re = re.search(r"^__version__ = \"([^\"]*)\"", fh.read(), re.MULTILINE)
assert version_re is not None, "Could not find version in colorlogging/__init__.py"
version: str = version_re.group(1)


setup(
    name="colorlogging",
    version=version,
    description="A simple utility package for Python logging with colors",
    author="Benjamin Bolte",
    url="https://github.com/kscalelabs/colorlogging",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.11",
    install_requires=requirements,
    tests_require=requirements_dev,
    extras_require={"dev": requirements_dev},
    packages=["colorlogging"],
)
