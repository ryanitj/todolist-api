from setuptools import find_packages, setup

project = "Todolist API"
version = "0.1.0"
setup(
    name = project,
    version = version,
    description = "an API for a todolist application",
    author = "Corp",
    packages = find_packages(exclude=["*.tests"]),
    include_packages_data = True,
    install_requires = [
        "Flask==3.0.3",
        "pydantic==2.4.2",
        "flask-swagger==0.2.14",
        "marshmallow==3.22.0"
        "flask-smorest==0.44.0"
        "Flask-SQLAlchemy==3.1.1"
        "Flask-Migrate==4.0.7"
        "psycopg2-binary==2.9.9"
    ]
)