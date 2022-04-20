import re
from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    # replace Markdown links (docs/[NAME].md with (https://nbpercent.readthedocs.io/en/latest/[NAME].html
    long_description = re.sub(
        r"\(docs/([A-Za-z-_]*).md",
        "(https://nbpercent.readthedocs.io/en/latest/\\1.html",
        f.read(),
    )

with open(path.join(this_directory, "nbpercent/version.py")) as f:
    version_file = f.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    version = version_match.group(1)

setup_args = dict(
    name="nbpercent",
    version=version,
    author="Marc Wouts",
    author_email="marc.wouts@gmail.com",
    description="Jupyter notebooks as Percent scripts with outputs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mwouts/nbpercent",
    packages=find_packages(exclude=["tests"]),
    tests_require=["pytest"],
    install_requires=[
        "nbformat>=5.1.0",
    ],
    python_requires=">=3.6",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Framework :: Jupyter",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Text Processing :: Markup",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)

# Call setup
setup(**setup_args)
