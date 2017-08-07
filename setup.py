from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call


def post_install():
    check_call('apt-get update', shell=True)
    check_call('apt-get install -y build-essential pkg-config glib2.0-dev libexpat1-dev libgirepository1.0-dev gobject-introspection libtiff5-dev libjpeg62-turbo-dev libexif-dev libgif-dev librsvg2-dev libpoppler-glib-dev libgsf-1-dev liblcms2-dev', shell=True)
    check_call('pip install https://github.com/pygobject/pycairo/releases/download/v1.13.2/pycairo-1.13.2.tar.gz', shell=True)
    check_call('cd /tmp && wget http://ftp.gnome.org/pub/GNOME/sources/pygobject/3.14/pygobject-3.14.0.tar.xz && tar xvf pygobject-3.14.0.tar.xz && cd pygobject-3.14.0 && ./configure && make install', shell=True)

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
