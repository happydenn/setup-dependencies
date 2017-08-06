from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call

class PostDevelopCommand(develop):
    def run(self):
        check_call('apt-get update'.split())
        check_call('apt-get install gnome-common'.split())
        develop.run(self)

class PostInstallCommand(install):
    def run(self):
        check_call('apt-get update'.split())
        check_call('apt-get install gnome-common'.split())
        install.run(self)

setup(
    name='setupdep',
    version='0.0.1',
    cmdclass={'develop': PostDevelopCommand, 'install': PostInstallCommand})
