from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call


def post_install():
    check_call('curl -sL https://deb.nodesource.com/setup_8.x | bash -', shell=True)
    check_call('apt-get update', shell=True)
    check_call('apt-get install -y nodejs', shell=True)

class PostDevelopCommand(develop):
    def run(self):
        post_install()
        develop.run(self)

class PostInstallCommand(install):
    def run(self):
        post_install()
        install.run(self)


setup(
    name='setupdep',
    version='0.0.1',
    cmdclass={'develop': PostDevelopCommand, 'install': PostInstallCommand})
