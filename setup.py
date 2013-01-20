from distutils.core import setup

setup(
    name='Neith',
    version='0.1dev',
    author='tronhammer',
    author_email='tron@tronnet.me',
    # scripts=['bin/install', 'bin/test'],
    url="http://pypi.python.org/pypi/Neith",
    license=open('LICENSE').read(),
    packages=['neith',],
    description="An open source python based command and control center for device management with uniform communication channels, still in dev!",
    long_description=open('README').read(),
    install_requires=[
        "Python >= 2.6",
    ],
)

# More details available at:
#   - http://guide.python-distribute.org/creation.html#general-packaging-guidelines-for-unix