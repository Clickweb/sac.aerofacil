# -*- coding: utf-8 -*-
"""Installer for the sac.aerofacil package."""

from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = \
    read('README.rst') + \
    read('docs', 'CHANGELOG.rst') + \
    read('docs', 'LICENSE.rst')

setup(
    name='sac.aerofacil',
    version='0.9',
    description="Implementação Plone do site Aerofácil (SAC/PR)",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='plone policy theme',
    author='Clickweb',
    author_email='info@clickweb.com.br',
    url='http://pypi.python.org/pypi/sac.aerofacil',
    license='BSD',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['sac'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Pillow',
        'Plone',
        'archetypes.schemaextender',
        'five.grok',
        'five.pt',
        'plone.api',
        'plone.app.dexterity [grok, relations]',
        'plone.app.drafts',
        'quintagroup.seoptimizer==4.3',
        'setuptools',
        'sc.embedder==1.0b3',
        'z3c.jbot==0.7.1',
    ],
    extras_require={
        'test': [
            'mock',
            'plone.app.testing',
            'unittest2',
        ],
        'develop': [
            'coverage',
            'flake8',
            'jarn.mkrelease',
            'niteoweb.loginas',
            'plone.app.debugtoolbar',
            'plone.reload',
            'Products.Clouseau',
            'Products.DocFinderTab',
            'Products.PDBDebugMode',
            'Products.PrintingMailHost',
            'Sphinx',
            'zest.releaser',
            'zptlint',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
