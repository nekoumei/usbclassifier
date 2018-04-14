from setuptools import setup, find_packages

try:
    with open('README.md') as f:
        readme = f.read()
except IOError:
    readme = ''

def _requires_from_file(filename):
    return open(filename).read().splitlines()

version = __import__('usbclassifier').__version__

setup(
    name='usbclassifier',
    version=version,
    url='https://github.com/nekoumei/usbclassifier',
    author='nekoumei',
    author_email='nekoumei@gmail.com',
    maintainer='nekoumei',
    maintainer_email='nekoumei@gmail.com',
    description='Bagging Classifier with Under Sampling',
    long_description=readme,
    packages=find_packages(),
    install_requires=_requires_from_file('requirements.txt'),
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Environment :: MacOS X',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ]
)