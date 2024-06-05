from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="chalk",
    version="1.0.0",
    description="A Python library for coloring text in the terminal or console.",
    author="James Glitch",
    author_email="james.glitchie@gmail.com",
    url="https://github.com/jamesGlitchie/chalk",
    packages=["chalk"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "Topic :: Software Development :: Libraries",
        "Topic :: Terminals",
        "Topic :: Utilities",
    ],
    python_requires=">=3.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
