from setuptools import setup
import re


with open("README.md") as fp:
    long_description = fp.read()


def parse_req_line(line):
    line = line.strip()
    if not line or line[0] == "#":
        return None
    return line


def load_requirements(file_name):
    with open(file_name) as fp:
        reqs = filter(None, (parse_req_line(line) for line in fp))
        return list(reqs)


def find_version():
    with open("edu/__init__.py") as fp:
        for line in fp:
            # __version__ = '0.1.0'
            match = re.search(r"__version__\s*=\s*'([^']+)'", line)
            if match:
                return match.group(1)
    assert False, "cannot find version"


install_requires = load_requirements("requirements.txt")
tests_require = load_requirements("requirements-dev.txt")


setup(
    name="edu",
    version=find_version(),
    packages=["edupy"],
    install_requires=install_requires,
    tests_require=tests_require,
    description="Full-Stack Educative application with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    maintainer="joshialonzo",
    maintainer_email="joshi.alonzo@gmail.com",
    url="https://github.com/joshialonzo/edupy",
)
