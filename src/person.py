from generator import Generator

class person:
    def __init__(self):
        Initials = Generator.genFullNameAndGender()
        self.firstName = Initials['name']
        self.lastName = Initials['surname']
        self.gender = Initials['gender']
        self.birthdate = Generator.genBirthDate()
        self.cpr = Generator.genCPR(self.gender, self.birthdate)

        self.phone = Generator.genPhoneNumber
        # self.address = address()

    #Debug
    def printPerson(self):
        print(f'First Name: {self.firstName} \nLast Name: {self.lastName} \nGender: {self.gender} \nBirthdate: {self.birthdate} \nCPR: {self.cpr}')
