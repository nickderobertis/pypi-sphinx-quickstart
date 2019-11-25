
[![](https://codecov.io/gh/whoopnip/pypi-sphinx-quickstart/branch/master/graph/badge.svg)](https://codecov.io/gh/whoopnip/pypi-sphinx-quickstart)

# pypi-sphinx-quickstart

## Overview

This repo is a template to use for starting a new Python package
which is hosted on PyPi and uses Sphinx for documentation
hosted on Github pages.

## Getting Started

Click the "Use this template" button at the top of the repo page, then 
fill out the name and description your new repo. Once you have the repo,
make the following edits.

### Setup Codecov

Go to [codecov.io](codecov.io), log in via Github, click Repositories then 
"Add new repository" and select this repository from the list. Copy the
token for Codecov to use in the next step.

### Adding Secrets

Go into settings and add the following secrets:
- `pypi_password`: Personal token for PyPI
- `gh_token`: Github personal access token
- `CODECOV_TOKEN`: [codecov.io](codecov.io) token for this project  

### `conf.py`

Edit `conf.py` in the main repo directory. This contains the main 
settings for the PyPi package. Fill out each setting with the 
details about your package.

### Adding Project Source

Delete the folder `py_qs_example`, and add your own package
with the name you set in `conf.PACKAGE_NAME`. 

### Adding Global Requirements to Build

If you do not already have `pipenv` installed, you will need to run:
```
pip install pipenv
```
Then regardless of whether you already had `pipenv` installed, you will
need to navigate to the repo folder and run:
```
pipenv update
```

### Setting up Documentation

Edit `docsrc/Makefile` to change `SPHINXPROJ` to set it to the name
you set in `conf.PACKAGE_NAME`.

Edit `docsrc/source/index.rst` to remove the example included files. Replace
with your own if you wish or entirely delete the My Module and 
My Package sections if don't wish to use the autosummary directive.

Edit `docsrc/source/tutorial.rst` to put your own tutorial, or remove it
and remove it from the `toctree` directive in `docsrc/source/index.rst`.

You may further modify Sphinx configuration in `docsrc/source/conf.py`
if you wish.

### Commit and Push

After the preceding steps, now commit your changes and push to `master`
if not done already. After a few minutes, Github Actions should create
a `gh-pages` branch which has the documentation HTML in it.

### Github Pages Setup

Go to repo settings, Github Pages section. For the Source dropdown, 
select "gh-pages branch". The settings page should reload,
and in the Github Pages section it should show the URL of your 
documentation. You should be able to see the documentation at the URL
after a few seconds, but it will still be the example documentation.

If "gh-pages branch" is not shown in the dropdown, you need to make one 
release commit and push it, so that the `gh-pages` branch will be added 
to your repo. After doing that, you can go into the repo settings
and select "gh-pages branch" as described.

## Built-in CI/CD

### On Every Push

Github Actions are used to automatically run the following steps on every push:
- Check Python syntax with `flake8`
- Run `pytest`
- Static typing checks with `mypy`

### When Branch is `master`

If the branch is the `master` branch, then it will also:
- Upload `pytest` results to `codecov`

#### If there is a change in `docsrc`

If the branch is the master branch, and there was a change in `docsrc`, it will do 
all the steps in On Every Push and When Branch is `master`, then it will:
- Build documentation HTML using Sphinx
- Create `gh-pages` branch and copy HTML there
- Push to `gh-pages` branch, which will update the hosted documentation 

#### If there is a change in the package version
f the branch is the master branch, and there was a change in the package version
in `conf.py`, it will do 
all the steps in On Every Push and When Branch is `master`, then it will:
- Build documentation HTML using Sphinx
- Create `gh-pages` branch and copy HTML there
- Push to `gh-pages` branch, which will update the hosted documentation 
- Build Python package
- Upload Python package to PyPI

## Regular Usage

Once everything is set up, just commit your changes. The built-in
CI/CD will take care of testing, build, and deployment of PyPI package
and documentation.

## Links

See the example 
[generated documentation here.](
https://whoopnip.github.io/pypi-sphinx-quickstart/
)
