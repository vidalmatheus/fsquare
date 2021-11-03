import pytest


@pytest.fixture
def fixture_example():
    return 'example'


def test_example(fixture_example):
    assert fixture_example == 'example'
