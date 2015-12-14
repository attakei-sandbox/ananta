# -*- coding:utf8 -*-
from setuptools import setup, find_packages


setup(
    name='ananta',
    version='0.0.0',
    url='https://github.com/attakei/ananta',
    description='AWS Lambda packager',
    long_description='',
    author='attakei',
    author_email='attakei@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='aws lambda',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[],
)
