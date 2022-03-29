import json
from operator import ge
from generator import Generator
from address import address

class person:
    def __init__(self):
        Initials = Generator.genFullNameAndGender()
        self.firstName = Initials['name']
        self.lastName = Initials['surname']
        self.gender = Initials['gender']
        self.birthdate = Generator.genBirthDate()
        self.cpr = Generator.genCPR(self.gender, self.birthdate)
        self.phone = Generator.genPhoneNumber()
        self.address = address()

    #Debug
    def printPerson(self):
        print(f'First Name: {self.firstName} \nLast Name: {self.lastName} \nGender: {self.gender} \nBirthdate: {self.birthdate} \nCPR: {self.cpr}')
        #Address
        print(f'Town: {self.address.town} \nZip Code: {self.address.zipCode} \nStreet Name and Number: {self.address.street} {self.address.number} \nFloor: {self.address.floor} \nDoor: {self.address.door}')

    def toJson(self):
        jsonString = ''
        personString = f'"firstName":"{self.firstName}", "lastName":"{self.lastName}", "gender":"{self.gender}", "birthdate":"{self.birthdate}", "cpr":"{self.cpr}", "phone":"{self.phone}",'
        personString = '{' + personString 
        addressString = str(self.address.__dict__).replace('{','')
        addressString = addressString.replace("'",'"')
        jsonString = personString + addressString
        return jsonString


