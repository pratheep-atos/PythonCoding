import pytest


@pytest.fixture()
def tip():
    print("abc")
    return ["giraffe", "people", "oilo"]


@pytest.fixture()
def datafeild():
    print("laexx")
    yield
    print("Printing")


@pytest.fixture(params=[("Chrome", "firefox"), ("people", "sunny")])
def confident(request):
    return request.param
