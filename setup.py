import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="taaled",
    version="0.20",
    author="Kristopher Kyle",
    author_email="kristopherkyle1@gmail.com",
    description="Text preprocessing for downstream linguistic analyses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LCR-ADS-Lab/TAALED",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)