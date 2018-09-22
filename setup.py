"""
Pythonish makefile for the project
"""

from distutils.cmd import Command
import subprocess
from setuptools import setup, find_packages

__version__ = "0.1"


class CodeCheck(Command):
    """Custom setup.py command to run code checking tools"""
    user_options = []

    def initialize_options(self):
        """Initialize options for this command"""
        pass

    def finalize_options(self):
        """Finalize options for this command"""
        pass

    def run(self):
        """Execute command and raise exception in case of failure"""
        return_value = subprocess.call('./codecheck.sh')
        if return_value:
            raise Exception('Code is not pure!')


setup(
    name="Text-to-speech",
    version=__version__,

    packages=find_packages(where=".", exclude=["tests", "tests.*"]),

    include_package_data=True,
    exclude_package_data={"": ["*.txt"]},

    install_requires=["pyttsx3", ],

    setup_requires=["setuptools-pep8", "setuptools-lint"],

    author="Chandan Kumar",
    author_email="chandanagni91@gmail.com",
    description="Python application to convert text to speech",
    long_description="This is a python application which converts text to speech" +
                     " using both online and offline approach.",
    project_urls={
        "Source Code": "https://github.com/cksagni91/text-to-speech.git",
    },

    test_suite="tests",
    cmdclass={'code_check': CodeCheck}
)
