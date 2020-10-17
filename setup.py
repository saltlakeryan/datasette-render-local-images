from setuptools import setup
import os

VERSION = "0.0.6"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-render-local-images",
    description="Render local images in the system using datasette plugin",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Kracekumar",
    url="https://github.com/kracekumar/datasette-render-local-images",
    project_urls={
        "Issues": "https://github.com/kracekumar/datasette-render-local-images/issues",
        "CI": "https://github.com/kracekumar/datasette-render-local-images/actions",
        "Changelog": "https://github.com/kracekumar/datasette-render-local-images/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_render_local_images"],
    entry_points={"datasette": ["render_local_images = datasette_render_local_images"]},
    install_requires=["datasette"],
    extras_require={
        "test": [
            "pytest",
            "pytest-asyncio",
            "httpx",
            "sqlite_utils",
            "coverage==5.3",
            "pytest-coverage",
        ]
    },
    tests_require=["datasette-render-local-images[test]"],
)
