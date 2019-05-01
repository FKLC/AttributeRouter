import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="AttributeRouter",
    version="1.0.0",
    description="An Attribute Router/Chainer For Any Class",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/FKLC/AttributeRouter",
    author="Fatih Kılıç",
    author_email="m.fatihklc0@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["attribute_router"],
)
