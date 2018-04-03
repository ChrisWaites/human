from setuptools import setup, find_packages

setup(
    name='human',
    version='0.1',
    description='API for querying human intelligence.',
    author='Chris Waites',
    author_email='cwaites10@gmail.com',

    license='MIT',
    url='http://github.com/ChrisWaites/human',
    scripts=['bin/human-cli']
    packages=find_packages(),
)
