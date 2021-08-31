from setuptools import setup, find_packages
setup(
    name='nothingness',
    version='1.0.0',
    license='MIT',
    author='Elisha Hollander',
    author_email='just4now666666@gmail.com',
    description="This is nothing, just a template for PyPI packages",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/donno2048/nothingness',
    project_urls={
        'Documentation': 'https://github.com/donno2048/nothingness#readme',
        'Bug Reports': 'https://github.com/donno2048/nothingness/issues',
        'Source Code': 'https://github.com/donno2048/nothingness',
    },
    python_requires='>=3.0',
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    classifiers=['Programming Language :: Python :: 3'],
    entry_points={ 'console_scripts': [ 'nothingness=nothingness.__main__:main' ] }
)
