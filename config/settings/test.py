# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# COVERAGE_MODULES = ['restful']
# TEST_RUNNER = 'config.testrunner.test_runner_with_coverage'
# sys.path.append(os.path.join(os.path.dirname(__file__), '../../verdors'))

try:
    from .base import *
except ImportError as e:
    raise e

DEBUG = False

INSTALLED_APPS += ('django_jenkins',)

PROJECT_APPS = (
    'service.customer',
    'service.resource',
    'service.frontend',
    'service.passport',
    'service.passport.registration',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'database', 'db.tests.sqlite3'),
    },
}

TEST_DEBUG = True
# TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Test runner
# TEST_RUNNER = 'django_coverage.coverage_runner.CoverageRunner'