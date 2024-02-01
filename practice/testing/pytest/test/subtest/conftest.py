import pytest


@pytest.fixture(scope='package', autouse=True)
def package_fixture():
    print('>> package_fixture started.')
    yield
    print('>> package_fixture ended.')


@pytest.fixture(name='subfixture')
def fixture_in_subpackage():
    print('sub package fixture')
    return ('sub package fixture')
