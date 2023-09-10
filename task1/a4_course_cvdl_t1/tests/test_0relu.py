import json
import os
from pathlib import Path

import pytest

from a4_course_cvdl_t1.relu import ReluLayer

TESTS_PATH_FILE = os.environ.get("A4_TESTS_PATH", Path(__file__).parent / 'data' / 'relu.json')


with open(TESTS_PATH_FILE) as f:
    TESTS = json.loads(f.read())


@pytest.fixture(params=TESTS, scope='module')
def test_data(request):
    return request.param


@pytest.fixture(scope='module')
def test_layer_cls():
    return ReluLayer

from a4_course_cvdl_t1.tests.base import TestLayer
