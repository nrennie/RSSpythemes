from setuptools import setup, find_packages

DESCRIPTION = 'RSS Palettes and Themes'
LONG_DESCRIPTION = 'Defines colour palettes and themes for RSS publications.'

# Setting up
setup(
        name="RSSpythemes", 
        version="1.0.0",
        author="Nicola Rennie",
        author_email="nrennie35@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        keywords=['python'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent"
        ]
)
