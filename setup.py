from setuptools import setup, find_packages

def readme():
    with open("README.md", "r") as fh:
        long_description = fh.read()
        return long_description


setup(
    name="prime-numbers-sisyphus",
    version="0.0.1",
    author="King of Ephyra",
    description="Sample 'package' to make fixture primes rather than calculate them.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/AndGasper/prime-numbers",
    packages=find_packages(),
    python_required=">3.7"
)