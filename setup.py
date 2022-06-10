import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="psmanager",
    version = "0.0.1",
    description = "psmanager(Password Manager) is a python package which helps managing passwords",
    long_description = README,
    long_description_content_type = "text/markdown",
    url = "https://github.com/saaemfairdi07/psmanager/",
    author = "Saaem Faridi",
    author_email = "<officialsaaem@gmail.com>",
    license = "MIT",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    packages = ["psmanager"],
    include_package_data =True,
    install_required = [],
)