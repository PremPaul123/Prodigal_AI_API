from setuptools import setup, find_packages

setup(
    name='prodigal-ai-api',
    version='0.1.0',
    description='A simple API package for Prodigal AI',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Prem Paul',
    author_email='premalladi2003@gmail.com',
    url='https://github.com/PremPaul123/Prodigal_AI_API',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
