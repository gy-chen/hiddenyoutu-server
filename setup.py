from setuptools import setup, find_packages

setup(
    name="hiddenyoutu_server",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        'flask',
        'flask-cors'
    ]
)
