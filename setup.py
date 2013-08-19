#!/usr/bin/env python

import sys
assert sys.version >= '2.7', "Requires Python v2.7 or above."
from setuptools import setup

setup(
    name = "django-mocky",
    version = "0.1",
    author = "J. Gabriel",
    author_email = "jgabriel.atx+mocky@gmail.com",
    url = "https://github.com/jongabriel/django-mocky",
    description = "Mocky is a simple app that allows to generate custom HTTP responses.",
    long_description = """Mocky is a simple app that allows to generate custom HTTP responses. 
                        It's helpful when you have to request a build-in-progress WS, when 
                        you want to mock the backend response in a singleapp, 
                        or when you want to test your WS client.
                        Credit and inspiration: https://github.com/studiodev/Mocky""",
    license = "MIT",
    packages = ["mocky"],
)