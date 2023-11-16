from setuptools import setup

setup(
    # package metadata
    name="multi-branching",
    description="Data Engineering utility functions",
    url="https://github.com/jeremytee97/multi-branching-poc",
    author="jtee",
    author_email="jtee@moneylion.com",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    # package setup
    version="1.0.0",
    # requirements
    python_requires=">=3.11",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.11",
    ],
)
