from pathlib import Path
from setuptools import setup

setup(
    name="json_wrapper",
    description="Easy to use JSON wrapper packed with features.",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type='text/markdown',
    url="https://github.com/RGBCube/json_wrapper",
    version="1.3.0",
    author="RGBCube",
    py_modules=["json_wrapper"],
    license="CC0 1.0 Universal"
)
