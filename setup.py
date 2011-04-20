from setuptools import setup, find_packages


setup(
    name = "system-session-bookings",
    version = "1.0",
    url = "http://github.com/carletes/system-session-bookings",
    license = "BSD",
    description = "System session booking for COS",
    author = "Carlos Valiente",
    packages = find_packages("src"),
    package_dir = {"": "src"},
    install_requires = ["setuptools"],
)

