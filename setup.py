from setuptools import setup, find_packages
import fping



setup(
    name='fping',
    version=fping.__version__,
    description='The fast ping',
    #url='git@github.com:rfschubert/ptolemaios-sdk-package.git',
    url='https://github.com/yuryrunx/fping.git',
    author=fping.__author__,
    author_email='yury@example.com',
    license=fping.__licence__,
    packages=['fping'],
    zip_safe=False
)