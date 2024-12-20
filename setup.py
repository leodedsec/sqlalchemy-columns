import os
from setuptools import setup, find_packages  # type: ignore

NAME = "sqlalchemy_columns"

DESCRIPTION = ""
URL = "https://github.com/leodedsec/sqlalchemy-columns.git"
LONG_DESCRIPTION = open(os.path.join(os.path.dirname(__file__), "README.md")).read()

AUTHOR = "leodedsec"
AUTHOR_EMAIL = ""
VERSION = "0.1.0"

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    include_package_data=True,
    zip_safe=False,
    keywords=[
        "sqlalchemy_columns"
        "sqlalchemy-columns",
        "sqlalchemy columns",
    ],
    setup_requires=[
        "wheel",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=["sqlalchemy>=2.0"],
    python_requires=">=3.10.0",
)
