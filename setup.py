import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    name="yolov7",
    py_modules=["yolov7"],
    version="1.0",
    packages=['models', 'utils', 'utils.aws', 'utils.wandb_logging'],
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    entry_points={},
    include_package_data=True,
    extras_require={'dev': ['pytest']},
)
