import io
import os
import re

import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


def read(fname, readlines=False):
    here = os.path.dirname(os.path.abspath(__file__))
    with io.open(os.path.join(here, fname), mode="rt", encoding="utf8") as f:
        return f.readlines() if readlines else f.read()


def get_version():
    init = read("staticrab/__init__.py")
    return re.search(r"__version__ = \"(.*?)\"", init).group(1)


setup(
    name="staticrab",
    version=get_version(),
    description="Fast correlation coefficients",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/staticrab/staticrab",
    author="Vladimír Kunc",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=read("requirements.txt", True),
    python_requires='>=3.8',
)
