from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="json_wrapper",
    description="Easy JSON wrapper packed with features",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/RGBCube/json_wrapper",
    version="1.0.2",
    author="RGBCube",
    py_modules=["json_wrapper"],
    license="CC0 1.0 Universal"
)
