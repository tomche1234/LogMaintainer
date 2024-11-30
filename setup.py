from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="1.0.0",
    author="Tom",
    author_email="tomche424@gmail.com",
    description="This package is for logging the function related",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tomche1234/LogMaintainer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11.3',
    install_requires=[
        # Add your package dependencies here
    ],
)
