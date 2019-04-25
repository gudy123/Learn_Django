import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__),'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__),os.pardir)))

setup(
    name = 'django-polls',
    version = '0.1',
    packages = find_packages(),
    include_package_data = True,
    license = 'BSD License',
    description = 'A simple Django app to conduct Web-based polls.',
    long_decription = README,
    url = 'http://www.example.com/',
    author = 'gudy',
    author_email = '1242018755@qq.com',
    classifiers = [
        'Enironment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'IntendedAudience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Ubuntu 17',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
)
