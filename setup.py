from setuptools import find_packages, setup

setup(
    name='evodoc',
    version='1.0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask-migrate',
        'flask-bcrypt',
        'pypandoc',
    ],
    setup_requires=[
        "pytest-runner",
    ],
    tests_require=[
        "pytest",
        "pytest-cov",
        'flask',
        'flask-sqlalchemy',
        'flask-migrate',
        'flask-bcrypt',
    ],
)
