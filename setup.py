from setuptools import setup, find_packages

setup(
    name="pyhook",
    version="0.1",
    packages=find_packages(),
    install_requires=["requests"],
    description="A simple Python library for sending webhooks",
    author="Your Name",
    url="https://github.com/yourusername/pyhook",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
