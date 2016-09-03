import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "evdev_redirector",
    version = "0.0.1",
    author = "Miroslav Tzonkov",
    author_email = "atvservice@mail.bg",
    description = ("Get touchpad events and transforms them to uinput events "),
    license = "GPL",
    keywords = "evedev zoom event touchpad touchpoint",
    url = "http://smooker.org/touchpad_redirector",
    packages=['evedev_redirector', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GPL License",
    ],
)
