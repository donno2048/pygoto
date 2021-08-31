from setuptools import setup, find_packages
setup(
    name='pygoto',
    version='1.0.0',
    license='MIT',
    author='Elisha Hollander',
    author_email='just4now666666@gmail.com',
    description="Use goto in Python",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/donno2048/pygoto',
    project_urls={
        'Documentation': 'https://github.com/donno2048/pygoto#readme',
        'Bug Reports': 'https://github.com/donno2048/pygoto/issues',
        'Source Code': 'https://github.com/donno2048/pygoto',
    },
    python_requires='>=3.0',
    packages=find_packages(),
    classifiers=['Programming Language :: Python :: 3']
)
