from typing import Sequence
from subprocess import run
from distutils.core import run_setup

import conf
import version


DISTRIBUTION_NAME = f'{conf.PACKAGE_NAME}-{version.__version__}'
DISTRIBUTION_PATH = f'dist/{DISTRIBUTION_NAME}'


def twine(main_command: str):
    command = f'twine {main_command} dist {DISTRIBUTION_PATH}'
    run(command, shell=True, check=True)


def upload_app(first_time: bool = False):
    run_setup('setup.py', script_args=['sdist', 'bdist_wheel'])
    if first_time:
        twine('register')
    twine('upload')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=f'Build and upload {conf.PACKAGE_NAME} to PyPi')
    parser.add_argument(
        '--first-time',
        action='store_true',
        help='Registers PyPi package as well as building and uploading, to be run only on the first time'
    )

    args = parser.parse_args()

    upload_app(first_time=args.first_time)