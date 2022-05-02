import pathlib
import os
from setuptools import setup, find_packages

VERSION = os.environ['VERSION']

DIR = pathlib.Path(__file__).parent
README = (DIR / "README.md").read_text()

setup(
    name="omniversion",
    version=VERSION,
    description="Omniversion Python integration",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/omniversion/omniversion",
    author="Layer9 GmbH",
    author_email="hello@layer9.berlin",
    license="AGPLv3.0",
    packages=find_packages(),
)
