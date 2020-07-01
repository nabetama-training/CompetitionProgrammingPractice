from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='CompetitionProgrammingPractice',
    version='0.1.0',
    description='Training',
    long_description=readme,
    author='Mao Nabeta',
    author_email='mao.nabeta@gmail.com',
    url='https://github.com/nabetama-training/CompetitionProgrammingPractice',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
