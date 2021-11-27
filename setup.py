from setuptools import setup, find_packages
from pathlib import Path


# get current directory
here = Path(__file__).parent


def get_long_description():
    """
    get long description from README.rst file
    """
    with here.joinpath("README.rst").open("r") as f:
        return f.read()


setup(
    name="cmon",
    version="0.0.3",
    description="FritzBox call monitor.",
    long_description=get_long_description(),
    url="https://github.com/keans/cmon",
    author="Ansgar Kellner",
    author_email="keans@gmx.de",
    python_requires=">=3.7",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="cmon",
    packages=find_packages(
        exclude=["contrib", "docs", "tests"]
    ),
    include_package_data=True,
    install_requires=[],
)
