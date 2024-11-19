# coding: utf-8

"""
    Autotab API

    AI that does your repetitive work end to end, with superhuman reliability.

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "autotab-ai"
VERSION = "0.0.4"
PYTHON_REQUIRES = ">= 3.8"
REQUIRES = [
    "urllib3 >= 1.25.3, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "aiohttp >= 3.8.4",
    "aiohttp-retry >= 2.8.3",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Autotab API",
    author="Planetary Computers",
    author_email="support@autotab.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Autotab API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    AI that does your repetitive work end to end, with superhuman reliability.
    """,  # noqa: E501
    package_data={"autotab": ["py.typed"]},
)
