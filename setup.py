from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='vwc.blog',
      version=version,
      description="Blogging facilities for berghausung site",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Vorwaerts Werbung GbR',
      author_email='cb@vorwaerts-werbung.de',
      url='http://dist.vorwaerts-werbung.de',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['vwc'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.api',
          'plone.app.dexterity [grok, relations]',
          'plone.namedfile [blobs]',
          'plone.formwidget.recaptcha',
          'collective.upload',
          'sc.social.like',
          'fourdigits.portlet.twitter',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
