from setuptools import setup, find_packages

def readme():
    with open("README.md", "r") as fh:
        long_description = fh.read()
        return long_description

setup(
    name="check-for-dependency-changes",
    version="1.0.0",
    author="Andres Gasper",
    description="Pre-commit hook to screen for dependency changes.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/AndGasper/prime-numbers/pre-commit-hooks/check-for-dependency-changes",
    packages=find_packages(),
    python_required=">3.7"
)
