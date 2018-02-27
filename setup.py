import os
from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), "r", encoding="utf-8") as fobj:
    long_description = fobj.read()

requires = [
    "click",
]

setup(
    name="zencore-json2csv",
    version="0.1.1",
    description="Convert json array data to csv.",
    long_description=long_description,
    url="https://github.com/appstore-zencore/zencore-json2csv",
    author="zencore",
    author_email="dobetter@zencore.cn",
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords=['zencore-json2csv'],
    packages=find_packages("src"),
    package_dir={"": "src"},
    zip_safe=False,
    include_package_data=True,
    package_data={
        "": ["*.*"],
    },
    requires=requires,
    install_requires=requires,
    scripts=[
        "src/scripts/json2csv.py",
        "src/scripts/json2csv",
    ],
)
