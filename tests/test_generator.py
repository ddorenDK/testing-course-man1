import pytest
from src.generator import Generator

#Unit Tests
#TODO
# ADD PROPER COMMENTS

def test_genFullNameAndGender():
    output = Generator.genFullNameAndGender()
    assert isinstance(output['name'], str)
    assert isinstance(output['surname'], str)
    assert isinstance(output['gender'], str)
    assert output['gender'] in ['male', 'female']

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

def test_genPhoneNumber():
    output = Generator.genPhoneNumber()
    allowedStarts = ('2','30','31','40','41','42','50','51','52','53','60','61','71','81','91','92','93','342','344','345','346','347','348','349','356','357','359','362','365','366','389','398','431','441','462','466','468','472','474','476','478','485','486','488','489','493','494','495','496','498','499','542','543','545','551','552','556','571','572','573','574','577','579','584','586','587','589','597','598','627','629','641','649','658','662','663','664','665','667','692','663','694','697','771','772','782','783','785','786','788','789','826','827','829')
    assert(len(output) == 8)
    assert(output.isnumeric)
    assert(isinstance(output, str))
    assert(output.startswith(allowedStarts))

    #test
    








