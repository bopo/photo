# Makefile six

PIP=$(VIRTUAL_ENV)/bin/pip
PY=$(VIRTUAL_ENV)/bin/python

.PHONY: clean-pyc clean-npm clean-build docs clean distclean clean-others npm req req.update pep8 bower apt run

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "distclean - remove all build, test, coverage, npm and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-npm - remove Python file artifacts"
	@echo "clean-others - remove Thumbs.db, etc file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "lint - check style with flake8"
	@echo "pep8 - check style with pep8"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "req - install project requirements"
	@echo "npm - install project npm modules"
	@echo "apt - install project apt-get package"
	@echo "bower - install project bower modules"
	@echo "req.update - update project requirements"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "dist - package"
	@echo "install - install the package to the active Python's site-packages"

clean: clean-build clean-others clean-pyc clean-test
distclean: clean-build clean-others clean-pyc clean-test clean-npm

clean-build:
	-rm -fr build/
	-rm -fr dist/
	-rm -fr .eggs/
	-find . -name '*.egg-info' -exec rm -fr {} +
	-find . -name '*.egg' -exec rm -f {} +
	-find . -name '*.log' -exec rm -f {} +

clean-others:
	-rm -fr static/
	-find . -name 'Thumbs.db' -exec rm -f {} \;
	-find . -name '*.tgz' -exec rm -f {} \;
	-find . -name '*.tar' -exec rm -f {} \;
	-find . -name '*.tar.gz' -exec rm -f {} \;

clean-pyc:
	-find . -name '*.pyc' -exec rm -f {} +
	-find . -name '*.pyo' -exec rm -f {} +
	-find . -name '*~' -exec rm -f {} +
	-find . -name '__pycache__' -exec rm -fr {} +

clean-npm:
	-rm -rf node_modules


clean-test:
	-rm -fr .tox/
	-rm -f .coverage
	-rm -fr htmlcov/

lint:
	flake8 liveapp tests

test:
	@$(PY) manage.py test

test-all:
	tox

coverage:
	-coverage run manage.py test
	-coverage report -m
	-coverage html
	-open htmlcov/index.html

docs:
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	-open docs/_build/html/index.html

run:
	@$(PY) manage.py runserver & open http://localhost:8000/ & fg

req:
	@$(PIP) install -r requirements.txt

apt:
	sudo apt-get install libjpeg8-dev libfreetype6-dev zlib1g-dev libssl-dev libffi-dev libxslt1-dev libxml2-dev python-dev

npm:
	-npm install

bower:
	-bower install

req.update:
	@$(PIP) install -U -r requirements.txt

pep8:
	@pep8 --filename="*.py" --ignore=W --first --show-source --statistics --count

release: clean
	python manage.py collectstatic --noinput
	gunicorn config.wsgi -w 4 -b 0.0.0.0:5000

dist: clean
	tar zcfv liveapp.tgz .

install: clean
	@$(PY) setup.py install
