from setuptools import setup,find_packages

with open('requirements.txt') as f:
    requirements=f.read().splitlines()


setup(
    name='AI TRAVEL Agent',
    version='0.1',
    author='mdzaheerjk',
    packages=find_packages(),
    install_requires=requirements
)