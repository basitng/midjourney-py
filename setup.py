from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.3'
DESCRIPTION = 'MidjourneyPy allows developers to easily use midjourney api without complications.'
LONG_DESCRIPTION = '''The MidjourneyPy APIRequest library provides a simplified and convenient way for developers to interact with the Midjourney API. With this library, developers can easily integrate Midjourney's powerful image processing capabilities into their applications without dealing with the complexities of manual API calls.'''

# Setting up
setup(
    name="midjourney-py",
    version=VERSION,
    author="Ajaga Abdulbasit (Code  Ninja)",
    author_email="basitng2004@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'ai', 'midjourney',
              'image', 'request', 'stable', 'stable difusion', 'difusion'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
