import pytest
from src.generator import Generator

#Unit Tests
#TODO
# ADD PROPER COMMENTS PLEASE

def test_genFullNameAndGender():
    output = Generator.genFullNameAndGender()
    assert isinstance(output['name'], str)
    assert isinstance(output['surname'], str)
    assert isinstance(output['gender'], str)
    assert (output['gender'] == 'male' or output['gender'] == 'female')

def test_genBirthDate():
    output = Generator.genBirthDate()
    assert (len(output) == 10)
    #TODO
    # Also check if date is valid

def test_genCPR():
    output = Generator.genCPR('male','12-12-1988')
    assert(len(output) == 11)
    #Test for males, last character is odd
    assert(int(output[-1:]) % 2 != 0)
    #Test for females, last character is even
    output = Generator.genCPR('female','12-12-1988')
    assert(int(output[-1:]) % 2 == 0)

def test_genStreet():
    output = Generator.genStreet()
    #Check if alphabetical
    assert(output.isalpha())

def test_genStreetNumber():
    output = Generator.genStreetNumber()
    #Check if is numeric
    assert(output[:-1].isnumeric() or output.isnumeric())

def test_genDoorNumber():
    output = Generator.genDoorNumber()
    assert(output.isnumeric())








