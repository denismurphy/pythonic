from setuptools import setup, find_packages

setup(
    name="pythonic",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    entry_points={},
    author="Denis Murphy",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown"
)