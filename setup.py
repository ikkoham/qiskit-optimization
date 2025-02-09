# This code is part of Qiskit.
#
# (C) Copyright IBM 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import setuptools
import inspect
import sys
import os

long_description = """Qiskit Optimization is a open-source library of quantum computing optimizations.
 """

requirements = [
    "qiskit-terra>=0.17.0",
    "scipy>=1.4",
    "numpy>=1.17",
    "docplex; sys_platform != 'darwin'",
    "docplex==2.15.194; sys_platform == 'darwin'",
    "setuptools>=40.1.0",
    "networkx>=2.2",
    "dataclasses; python_version < '3.7'"
]

if not hasattr(setuptools, 'find_namespace_packages') or not inspect.ismethod(setuptools.find_namespace_packages):
    print("Your setuptools version:'{}' does not support PEP 420 (find_namespace_packages). "
          "Upgrade it to version >='40.1.0' and repeat install.".format(setuptools.__version__))
    sys.exit(1)

VERSION_PATH = os.path.join(os.path.dirname(__file__), "qiskit_optimization", "VERSION.txt")
with open(VERSION_PATH, "r") as version_file:
    VERSION = version_file.read().strip()

setuptools.setup(
    name='qiskit-optimization',
    version=VERSION,
    description='Qiskit Optimization: A library of quantum computing optimizations',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Qiskit/qiskit-optimization',
    author='Qiskit Optimization Development Team',
    author_email='hello@qiskit.org',
    license='Apache-2.0',
    classifiers=(
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering"
    ),
    keywords='qiskit sdk quantum optimization',
    packages=setuptools.find_packages(include=['qiskit_optimization', 'qiskit_optimization.*']),
    install_requires=requirements,
    include_package_data=True,
    python_requires=">=3.6",
    extras_require={
        'cplex': ["cplex; python_version < '3.9'"],
        'cvx': ['cvxpy'],
    },
    zip_safe=False
)
