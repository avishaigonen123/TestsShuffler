import os

import pytest


@pytest.fixture()
def tests_data_dir():
    test_root_dir = os.path.dirname(os.path.realpath(__file__))
    test_data_dir = os.path.join(test_root_dir, "data")
    return test_data_dir
