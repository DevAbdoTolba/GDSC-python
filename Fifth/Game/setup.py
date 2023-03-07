from setuptools import setup, find_packages

setup(
    name='Game',
    version='0.1.0',
    description='A simple Python game package',
    author='Abdo Tolba',
    author_email='DevAbdoTolba@gmail.com',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'game = Game.StartGame:main'
        ]
    }
)
