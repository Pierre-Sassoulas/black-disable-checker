from setuptools import find_namespace_packages, setup

with open("README.md", "r", encoding="utf-8") as r:
    README = r.read()

setup(
    author="Pierre Sassoulas",
    author_email="pierre.sassoulas@gmail.com",
    long_description=README,
    long_description_content_type="text/markdown",
    name="black-disable-checker",
    version="0.0.1",
    packages=["black_disable_checker"],
    entry_points={"console_scripts": ["black-disable-checker=black_disable_checker.__main__:main"]},
    install_requires=[],
    url="https://github.com/Pierre-Sassoulas/black-disable-checker/",
    zip_safe=True,
)
