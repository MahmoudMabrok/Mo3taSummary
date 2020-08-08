"""Setup script for codesummary"""

import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="codesummary",
    version="1.0.0",
    description="provide code summary, each language used with LOC counts",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/MahmoudMabrok/Mo3taSummary",
    author="Mahmoud Mabrok",
    author_email="mahmoudmabrok3579@gmail.com",
    license="Apache",
    classifiers=[
        "License :: OSI Approved :: Apache License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["summary"],
    include_package_data=True,
    install_requires=[
        "beautifultable"
    ],
    entry_points={"console_scripts": ["codesummary=summary.__main__:main"]},
)
