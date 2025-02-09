#Fixtures
import pytest


@pytest.fixture(scope="module") # function - for every test module - once
def preWork():
    print('Setup browser instance')


def test_check_1(preWork):
    print(' This is a first test')

def test_check_2(preWork):
    print(' This is a second test')