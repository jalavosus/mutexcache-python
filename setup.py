import pathlib
from setuptools import setup

BASE_DIR = pathlib.Path(__file__).parent

README = (BASE_DIR / "README.md").read_text()

setup(
    name="mutexcache",
    version="0.1.1",
    description="Dynamically created, cached mutexes in Python.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jalavosus/mutexcache-python",
    author="jalavosus",
    author_email="alavosus.james@gmail.com",
    license="MIT",
    packages=["mutexcache"],
    include_package_data=True,
    install_requires=["expiringdict"]
)