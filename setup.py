from setuptools import setup

setup(
    name='human',
    version='0.1',
    description='API for querying human intelligence.',
    url='http://github.com/ChrisWaites/human',
    author='Chris Waites',
    author_email='cwaites10@gmail.com',
    license='MIT',
    packages=['human'],
    scripts=['bin/cli']
    zip_safe=False
)
