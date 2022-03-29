import pytest

from src.generator import Generator



def test_genFullNameAndGender():
    output = Generator.genFullNameAndGender()
    assert isinstance(output['name'], str)
