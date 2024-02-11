from setuptools import setup, find_packages

setup(
    name='refine',
    version='0.1.0',
    author='Ishan Dutta',
    author_email='ishandutta0098@gmail.com',
    packages=find_packages(),
    url='https://github.com/ishandutta0098/refine',
    license='MIT',
    description='A Python package for cleaning data.',
    long_description=open('README.md').read(),
    install_requires=[
        # Add your dependencies here
        # e.g., 'pandas>=1.0.0',
    ],
    python_requires='>=3.6',
)
