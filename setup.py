import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pywmit",
    version="0.1.1",
    author="Luigi Russo",
    author_email="russo.1699981@studenti.uniroma1.it",
    description="A simple package to interact Wikipedia pages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lrusso96/pywm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['mwparserfromhell', 'mwklient'],
    test_suite='nose.collector',
    tests_require=['nose'],
)
