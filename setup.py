"""
Setup script for the package
"""

from setuptools import setup

with open("README.md") as readme_file:
    README = readme_file.read()

with open("requirements.txt") as req_file:
    REQ = req_file.read()


setup(
    name="pi calculator",
    version="0.1.0",
    description="Compute pi with the monte carlo technic",
    long_description=README,
    author="Alain Girard",
    author_email="alaingirardvd@gmail.com",
    url="https://github.com/Allain18/pimontecarlo",
    license="MIT License",
    keywords="pi monte carlo",
    install_requires=REQ,
    py_modules=["pi_montecarlo"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    test_suite="test",
    entry_points={
        "console_scripts": [
            "pi=pi_montecarlo:main",
        ]
    },
)
