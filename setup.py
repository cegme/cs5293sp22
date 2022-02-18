# python setup.py build
# python -m build

from setuptools import setup, find_packages

setup(
    name="tweetcounter",
    version="0.1",
    author="class",
    author_email="sridhar@ou.edu",
    packages=find_packages(exclude=("test", "docs")),
    setup_requires=["pytest-runner"],
    test_require=["pytest"],
)
