from setuptools import setup, find_packages

version = '0.1dev'

long_description = "Changes:\n\n%s" % open('CHANGES.txt').read()

setup(
    name='opencore_cleantheme',
    version=version,
    description='A theme for OpenCore Software',
    long_description=long_description,
    # Get more strings from https://pypi.org/pypi?:action=list_classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Plugins",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Office/Business :: Office Suites",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='Plone theme OpenCore Software',
    author='Ethan Jucovy',
    author_email='opencore-dev@lists.coactivate.org',
    url='https://github.com/socialplanning/opencore_cleantheme',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['opencore', 'opencore.themes'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        ],
    entry_points="""
      # -*- Entry points: -*-
      [topp.zcmlloader]
      opencore = opencore.themes.cleantheme
        """,
    )

