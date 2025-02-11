import pytest

@pytest.fixture(scope="session") # function - for every test; module - once; session - once for set of tests
def preSetupWork():
    print('')
    print('Setup browser instance')