from setuptools import setup

setup(
    name='analogy',
    version='0.0.1',

    package_dir={'analogy': 'analogy'},
    packages=['analogy'],

    entry_points={
        'console_scripts': [
            'eval-analogy = analogy.main:__main__'
        ]
    }
)