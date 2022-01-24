from setuptools import find_packages, setup

import cli

NAME = "gui"


def read(filename):
    try:
        with open(filename) as fp:
            content = fp.read().split("\n")
    except FileNotFoundError:
        content = []
    return content


setup(
    author="Quinten Roets",
    author_email="quinten.roets@gmail.com",
    description="gui",
    name=NAME,
    version="1.0",
    py_modules=["gui"],
    setup_requires=read("setup_requirements.txt"),
    install_requires=read("requirements.txt"),
)


cli.install(*read("packages.txt"))
