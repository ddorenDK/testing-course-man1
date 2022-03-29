from generator import Generator
import pytest


def test_genFullNameAndGender():
    output = Generator.genFullNameAndGender()
    assert isinstance(output['name'], str)
