# coding:utf-8

from setuptools import setup

setup(
    name = 'errant',
    version = 'v1.0',
    packages = ['scripts'],
    package_data = {'errant':['resources/en_GB-large.txt','resources/en-ptb-map']},
    install_requires = [
        'spacy==1.9.0',
        'nltk==3.3'
    ]
)