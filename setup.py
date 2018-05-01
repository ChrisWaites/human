from setuptools import setup, find_packages

setup(
    name='people',
    version='0.1.8',
    description='Human Interaction API',
    author='Chris Waites',
    author_email='cwaites10@gmail.com',

    license='MIT',
    url='http://github.com/ChrisWaites/people',
    packages=find_packages(),
    install_requires=['coreapi', 'requests'],
)
