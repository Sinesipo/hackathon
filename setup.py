from setuptools import setup, find_packages

setup(
    name='myPack',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Sinesipo/myPack.git',
    author='Sinesipo Mbasa',
    author_email='smbasa1818@gmail.com'
)
