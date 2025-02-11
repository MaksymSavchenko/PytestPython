#Fixtures
import pytest

@pytest.fixture(scope="module") # function - for every test; module - once; session - once for set of tests
def preWork():
    print('')
    print('Setup module instance')
    return "fail"

@pytest.fixture(scope="function") # function - for every test; module - once; session - once for set of tests
def secondWork():
    print('')
    print('Setup secondWork instance')
    yield #pause and resume after finish all executions
    print('')
    print('tear down validation')

@pytest.mark.smoke
def test_check_1(preWork, secondWork):
    print('')
    print(' This is a first test')
    assert preWork == "fail"

@pytest.mark.skip #skip test
def test_check_2(preSetupWork, secondWork):
    print('')
    print(' This is a second test')