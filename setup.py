from setuptools import setup, find_packages
import os

version = '0.1dev'

setup(
    name='opencore_cleantheme',
    version=version,
    description='',
    classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    keywords='',
    author='Ethan Jucovy',
    author_email='opencore-dev@lists.coactivate.org',
    url='',
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
