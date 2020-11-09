import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.PohaApplicationGroup8',
      version='0.0.1',
      description=('A docassemble extension for POHA applications.'),
      long_description="# docassemble-openlcbr\r\nA docassemble package for case outcome prediction using the analogical reasoning features of openclbr.\r\n\r\n[This post](https://medium.com/@jason_90344/legal-expert-systems-just-got-smarter-e7e12b75e872) is a primer on what an analogical reasoner does, and why it's so important to have one in the open-source toolkit.\r\n\r\n[This post](https://medium.com/@jason_90344/automating-case-based-reasoning-by-analogy-a-deep-dive-a1b015f234dd) provides a full explanation of how the IBP algorithm, which docassemble-openclbr implements, works.",
      long_description_content_type='text/markdown',
      author='Constance Tay, Tan Zay Hua, Victoria Phua',
      author_email='zhtan.2018@law.smu.edu.sg',
      license='The MIT License (MIT)',
      url='form.poha.application.group8',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/PohaApplicationGroup8/', package='docassemble.PohaApplicationGroup8'),
     )

