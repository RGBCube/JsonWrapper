from setuptools import setup

readme = ""
with open("README.md") as file:
    readme = file.read()

setup(
    name="json_wrapper",
    description="Easy JSON wrapper packed with features",
    url="https://github.com/RGBCube/json_wrapper",
    version="1.0",
    author="RGBCube",
    py_modules=["json_wrapper"],
    license="CC0 1.0 Universal"
)