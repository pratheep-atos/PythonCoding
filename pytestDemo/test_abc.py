import pytest


@pytest.mark.usefixtures("tip")
class Test:

    def test_firstprgm(self, tip):
        print(tip)


def test_pageing(confident):
    print(confident[1])